# 导入需要的库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# ====================== 1. 准备数据 ======================

# 定义各国家的实际出口量（和你原图的数据完全对应）
US_actual = np.array([1000,400,360,1402.2,1340,414,182,694,600,350,330,1000,500,300,435,979,600,350,50])
Brazil_actual = np.array([1163.4,939,679,1199,1200,1400,1000,1840,1200,2000,1800,1996,1500,2100,1600,2265,1454,2732,3184])
Argentina_actual = np.array([105,90,60,120,85,110,60,110,65,40,25,70,40,35,75,260,15,30,120])

# 定义美国对华大豆关税（2021Q1-2024Q4为10%，2025Q1-2025Q3为20%、34%、10%）
tariff = np.array([10]*16 + [20, 34, 10])

# 计算总进口量（三国出口量之和）
total_import = US_actual + Brazil_actual + Argentina_actual

# 根据数据长度生成季度时间序列，确保与数据长度一致并避免 'Q' 的弃用问题
# 使用 `Q-DEC` 以每年12月为季度末，起始选择 2021 年第一季度末日期
t = pd.date_range(start='2021-03-31', periods=len(US_actual), freq='Q-DEC')


# ====================== 2. 定义CMS模型核心函数 ======================
def calculate_cms_with_weights(
    actual_data,  # 某国的实际出口量
    total_import, # 总进口量
    base_period_slice  # 基准期的切片（比如slice(0, 12)表示前12个季度）
):
    """
    带时间权重的CMS模型计算函数
    作用：计算某国的CMS预测值，并返回预测结果
    """
    # 1. 提取基准期的数据
    base_actual = actual_data[base_period_slice]
    base_total = total_import[base_period_slice]
    
    # 2. 计算基准期的市场份额（某国出口/总进口）
    base_share = base_actual / base_total
    
    # 3. 给基准期加时间权重：近期数据权重更高（权重从0.5到1.5递增）
    weights = np.linspace(0.5, 1.5, len(base_actual))  # 生成权重数组
    weighted_base_share = np.average(base_share, weights=weights)  # 加权平均市场份额

    # 4. 基准预测（假设市场份额不变）
    base_pred_full = total_import * weighted_base_share

    # 5. 估计基准期的竞争力效应（实际 - 基准预测在基准期）
    base_pred_base = base_total * weighted_base_share
    comp_effect_base = base_actual - base_pred_base

    # 6. 两种合理的竞争力投影方式：
    #  - mean: 使用基准期竞争力效应的均值，认为竞争力带来的偏差为常数
    #  - trend: 在基准期上拟合线性趋势并对整个序列外推
    n_total = len(actual_data)
    n_base = len(base_actual)
    if n_base >= 2:
        x_base = np.arange(n_base)
        # 线性拟合 comp_effect_base ~ time
        coeffs = np.polyfit(x_base, comp_effect_base, 1)  # slope, intercept
        x_full = np.arange(n_total)
        comp_effect_trend_full = np.polyval(coeffs, x_full)
    else:
        coeffs = (0.0, float(np.mean(comp_effect_base)))
        comp_effect_trend_full = np.full(n_total, coeffs[1])

    comp_effect_mean = float(np.mean(comp_effect_base))
    comp_effect_mean_full = np.full(n_total, comp_effect_mean)

    # 7. 生成两套 CMS 预测：基准+均值偏差、基准+趋势偏差
    cms_pred_mean = base_pred_full + comp_effect_mean_full
    cms_pred_trend = base_pred_full + comp_effect_trend_full

    return cms_pred_trend, cms_pred_mean, weighted_base_share, base_pred_full, coeffs, comp_effect_mean


# ====================== 3. 调整基准期并计算CMS预测值 ======================
# 调整基准期：选择2021Q1-2023Q4（前12个季度，共12个数据点）
base_period = slice(0, 12)  # 0到11是前12个季度（Python切片是左闭右开）

# 计算美国的CMS预测值（返回：trend预测、mean预测、加权基准份额、基准预测、trend系数、mean偏差）
US_cms_trend, US_cms_mean, US_weighted_share, US_base_pred, US_trend_coeffs, US_comp_mean = calculate_cms_with_weights(US_actual, total_import, base_period)
# 计算巴西的CMS预测值
Brazil_cms_trend, Brazil_cms_mean, Brazil_weighted_share, Brazil_base_pred, Brazil_trend_coeffs, Brazil_comp_mean = calculate_cms_with_weights(Brazil_actual, total_import, base_period)


# ====================== 4. 计算拟合度（评估模型效果） ======================
US_r2_trend = r2_score(US_actual, US_cms_trend)
US_r2_mean = r2_score(US_actual, US_cms_mean)
Brazil_r2_trend = r2_score(Brazil_actual, Brazil_cms_trend)
Brazil_r2_mean = r2_score(Brazil_actual, Brazil_cms_mean)
print(f"美国出口拟合度R² (trend预测)：{US_r2_trend:.4f}")
print(f"美国出口拟合度R² (mean预测)：{US_r2_mean:.4f}")
print(f"巴西出口拟合度R² (trend预测)：{Brazil_r2_trend:.4f}")
print(f"巴西出口拟合度R² (mean预测)：{Brazil_r2_mean:.4f}")


# ====================== 5. 绘制对比图 ======================
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']  # 解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12), sharex=True)

# 上图：三国实际出口量（US, Brazil, Argentina）
ax1.plot(t, US_actual, 'bo-', label='US (实际出口)')
ax1.plot(t, Brazil_actual, 'y^-', label='Brazil (实际出口)')
ax1.plot(t, Argentina_actual, 'g*-', label='Argentina (实际出口)')
ax1.set_title('各国大豆对华实际出口量', fontsize=14, fontweight='bold')
ax1.set_ylabel('出口量 (吨)', fontsize=12)
ax1.legend()
ax1.grid(alpha=0.3)

# 下图：两国实际与CMS趋势预测（US 与 Brazil）
ax2.plot(t, US_actual, 'b.-', label='US (实际出口)', alpha=0.8)
ax2.plot(t, US_cms_trend, 'b-.', linewidth=2, label=f'US (CMS预测 - trend, slope={US_trend_coeffs[0]:.2f})')
ax2.plot(t, Brazil_actual, 'y.-', label='Brazil (实际出口)', alpha=0.8)
ax2.plot(t, Brazil_cms_trend, 'y-.', linewidth=2, label=f'Brazil (CMS预测 - trend, slope={Brazil_trend_coeffs[0]:.2f})')
ax2.set_title('CMS模型：实际出口 vs CMS趋势预测', fontsize=14, fontweight='bold')
ax2.set_xlabel('季度', fontsize=12)
ax2.set_ylabel('出口量 (吨)', fontsize=12)
ax2.legend()
ax2.grid(alpha=0.3)

# 将 x 轴刻度标签格式化为季度（如 2021Q1），但不改变坐标数据或刻度位置
quarter_labels = [f"{d.year}Q{((d.month-1)//3)+1}" for d in t]
ax2.set_xticks(t)
ax2.set_xticklabels(quarter_labels, rotation=45, ha='right')

plt.tight_layout()
plt.show()