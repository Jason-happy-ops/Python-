# 导入需要的库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.metrics import r2_score

# ====================== 1. 准备数据 ======================
# 定义时间序列：按数据长度生成季度时间（确保与数据同长）
t = pd.period_range(start='2021Q1', periods=19, freq='Q').to_timestamp()

# 定义各国家的实际出口量（和你原图的数据完全对应）
US_actual = np.array([1000,400,360,1402.2,1340,414,182,694,600,350,330,1000,500,300,435,979,600,250,50])
Brazil_actual = np.array([1163,939,679,1199,1200,1400,1000,1840,1200,2000,1800,1996,1500,2100,1600,2265,1454,2772,3184])
Argentina_actual = np.array([105,90,60,120,85,110,60,110,65,40,25,70,40,35,75,260,15,30,120] )

# 定义美国对华大豆关税（2021Q1-2024Q4为10%，2025Q1-2025Q3为20%、34%、10%）
tariff = np.array([10]*16 + [20, 34, 10])

# 计算总进口量（三国出口量之和）
total_import = US_actual + Brazil_actual + Argentina_actual


# ====================== 2. 定义CMS模型核心函数 ======================
def calculate_cms_with_weights(
    actual_data,  # 某国的实际出口量
    total_import, # 总进口量
    base_period_slice  # 基准期的切片（比如slice(0, 12)表示前12个季度）
):
    """
    带时间权重的CMS模型计算函数
    作用,计算某国的CMS预测值,并返回预测结果
    """
    # 1. 提取基准期的数据
    base_actual = actual_data[base_period_slice]
    base_total = total_import[base_period_slice]
    
    # 2. 计算基准期的市场份额（某国出口/总进口）
    base_share = base_actual / base_total
    
    # 3. 给基准期加时间权重：近期数据权重更高（权重从0.5到1.5递增）
    weights = np.linspace(0.5, 1.5, len(base_actual))  # 生成权重数组
    weighted_base_share = np.average(base_share, weights=weights)  # 加权平均市场份额
    
    # 4. 计算CMS模型的各部分
    # 基准预测值：总进口量 × 加权基准市场份额（假设市场份额不变的情况）
    base_pred = total_import * weighted_base_share

    # 如果直接把 comp_effect = actual - base_pred 全部加回，则 cms_pred==actual，
    # R^2=1 且无预测意义。为提高 2025 年前的拟合度，我们用基准期的 comp_effect
    # （带时间权重）来拟合一个线性趋势（简单可解释），再把该趋势投影到整个期。
    comp_effect_series = actual_data - base_pred

    # 基准期索引（0,1,...,len(base_actual)-1）
    x_base = np.arange(len(base_actual))
    # 使用加权线性回归拟合基准期的竞争力效应趋势（degree=1），权重为 weights
    # polyfit 支持权重参数 w
    coeffs = np.polyfit(x_base, comp_effect_series[base_period_slice], 1, w=weights)
    a, b = coeffs  # comp_effect ≈ a*t + b

    # 对全期进行预测（包括历史和未来），使得预测在基准期内能跟随历史趋势
    x_full = np.arange(len(actual_data))
    comp_effect_pred = a * x_full + b

    # 最终CMS预测值：基准预测值 + 预测的竞争力效应趋势
    cms_pred = base_pred + comp_effect_pred

    # 返回 cms_pred、加权基准份额以及预测的竞争力效应序列（便于绘图/检查）
    return cms_pred, weighted_base_share, comp_effect_pred


# ====================== 3. 调整基准期并计算CMS预测值 ======================
# 调整基准期：选择2021Q1-2023Q4（前12个季度，共12个数据点）
base_period = slice(0, 12)  # 0到11是前12个季度（Python切片是左闭右开）

# 计算美国的CMS预测值
US_cms_pred, US_weighted_share, US_comp_effect = calculate_cms_with_weights(US_actual, total_import, base_period)
# 计算巴西的CMS预测值
Brazil_cms_pred, Brazil_weighted_share, Brazil_comp_effect = calculate_cms_with_weights(Brazil_actual, total_import, base_period)


# ====================== 4. 计算拟合度（评估模型效果） ======================
US_r2 = r2_score(US_actual, US_cms_pred)
Brazil_r2 = r2_score(Brazil_actual, Brazil_cms_pred)
print(f"US export R²: {US_r2:.4f}")
print(f"Brazil export R²: {Brazil_r2:.4f}")


# ====================== 5. 绘制对比图 ======================
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']  # 解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12), sharex=True)

# Top: actual exports by country
ax1.plot(t, US_actual, 'bo-', label='US (Actual exports)')
ax1.plot(t, Brazil_actual, 'y^-', label='Brazil (Actual exports)')
ax1.plot(t, Argentina_actual, 'g*-', label='Argentina (Actual exports)')
ax1.set_title('Actual soybean exports to China by country', fontsize=14, fontweight='bold')
ax1.set_ylabel('Exports (tons)', fontsize=12)
ax1.legend()
ax1.grid(alpha=0.3)

# Bottom: Actual vs CMS predictions
ax2.plot(t, US_actual, 'bo-', label='US (Actual exports)')
ax2.plot(t, US_cms_pred, 'b--', label=f'US (CMS prediction, weighted base share={US_weighted_share:.4f})')
ax2.plot(t, Brazil_actual, 'y^-', label='Brazil (Actual exports)')
ax2.plot(t, Brazil_cms_pred, 'y--', label=f'Brazil (CMS prediction, weighted base share={Brazil_weighted_share:.4f})')
ax2.set_title('CMS Model: Actual vs Predicted Exports', fontsize=14, fontweight='bold')
ax2.set_xlabel('Quarter', fontsize=12)
ax2.set_ylabel('Exports (tons)', fontsize=12)
ax2.legend()
ax2.grid(alpha=0.3)

# Set x-axis ticks to quarter units and label them as 'YYYYQn'
# t is a DatetimeIndex of quarter start timestamps; convert to period labels
quarter_labels = t.to_period('Q').astype(str)
# Place a tick at every timestamp in t and rotate labels for readability
ax2.set_xticks(t)
ax2.set_xticklabels(quarter_labels, rotation=45, ha='right')

plt.tight_layout()

# 调试输出当前 matplotlib 后端，帮助定位显示问题
print("matplotlib backend:", mpl.get_backend())

# 作为回退：先保存到文件，这样即使 GUI 无法弹窗也能查看图片
out_path = 'cms_plot.png'
try:
    fig.savefig(out_path, dpi=200)
    print(f"Plot saved to: {out_path}")
except Exception as e:
    print(f"Error saving plot: {e}")

# 尝试显示图像；若抛出异常则已经有保存的文件可查看
try:
    plt.show()
except Exception as e:
    print(f"plt.show() raised an exception: {e}")