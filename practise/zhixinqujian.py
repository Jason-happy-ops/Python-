import numpy as np
import scipy.stats as stats
import math
import matplotlib.pyplot as plt
import random 


np.random.seed(42)  # 固定随机种子，确保每次运行结果一致
data = np.random.exponential(scale=10, size=100) + 40

#正态性检验
def checkout(data):
    stat,p_value = stats.shapiro(data)
    if p_value > 0.05:
        print("样本服从正态分布")
    else:
        print("样本不服从正态分布")



n = len(data)  #样本个数
sample_mean = np.mean(data)  #样本均值
sample_std = np.std(data, ddof=1)  #样本标准差，ddof=1表示使用样本标准差公式进行无偏估计

standard_error = sample_std / np.sqrt(n)  # σ/√n 标准误差

z_core = 1.96   #95%置信区间对应的z值
margin_of_error = z_core * standard_error  # 误差范围

max_value = sample_mean + margin_of_error
min_value = sample_mean - margin_of_error

print(f"样本均值为{sample_mean:.2f}")
print(f"95%置信区间为({min_value:.2f},{max_value:.2f}")


plt.figure(figsize=(6, 4))

plt.errorbar(
    x=0,                      # x轴位置（单组数据设为0即可）
    y=sample_mean,            # 均值（y轴核心值）
    yerr=margin_of_error,     # 置信区间的误差范围（上下各margin_of_error）
    fmt='o',                  # 均值点的样式（圆形）
    color='blue',             # 整体颜色
    ecolor='red',             # 误差棒（置信区间）颜色
    elinewidth=2,             # 误差棒线宽
    markersize=8,             # 均值点大小
    capsize=5,                # 误差棒两端横线长度（增强可读性）
    label='95%置信区间'
)

# 基础标注（仅必要内容）
plt.xticks([0], ['样本均值'])  # x轴仅显示“样本均值”
plt.ylabel('数值')
plt.title('基于errorbar的置信区间展示')
plt.legend()
plt.grid(alpha=0.3)

# 显示均值数值（可选，增强可读性）
plt.text(0, sample_mean, f' {sample_mean:.2f}', va='bottom', ha='center')

plt.show()