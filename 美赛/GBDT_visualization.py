from matplotlib import pyplot as plt
from GBDT_tools1 import train_gbdt_model
from GBDT_data import df2
import numpy as np


# 1. 获取赢的概率和横坐标数据
result = train_gbdt_model()
x = df2['point_no'].values  # 回合数
y = result           # 赢的概率

sorted_idx = np.argsort(x)  # 按回合数升序排序
x_sorted = x[sorted_idx]
y_sorted = y[sorted_idx]
step = 30
x_line = x_sorted[::step]   # 每10个点取一个横坐标
y_line = y_sorted[::step]

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号（避免坐标轴负号乱码

# 2. 极简绘制散点图（核心！）
plt.figure(figsize=(25, 8))  # 画布拉宽，横坐标区间自然变大
# 点设为最小（s=1），透明度拉低（alpha=0.5），颜色选浅红避免刺眼


plt.axhline(y=0.5, color='blue', linestyle='--', linewidth=2)

# 3. 仅保留必要标签，不搞多余美化
plt.xlabel("Point Number")
plt.ylabel("Predicted Win Probability")
plt.title("Win Probability by Point Number")

# 4. 横坐标拉到最大（自动适配数据的最大/最小值）
plt.xlim(x.min(), x.max())
plt.ylim(0, 1)  # 概率固定0-1

plt.tight_layout()
plt.text(
    x=300,                  # 标签横坐标（右上角）
    y=0.8,                  # 标签纵坐标（右上角）
    s="The proportion of points below the 50% baseline is 60.84%.",           # 自定义标签内容（换行用\n）
    fontsize=11,              # 文字大小
    ha='right',               # 文字右对齐（紧贴右上角）
    va='top',                 # 文字上对齐
    bbox=dict(                # 标签背景框（美化+防遮挡）
        boxstyle='round,pad=0.6',  # 圆角+内边距
        facecolor='white',         # 背景色（白色）
        alpha=0.9,                 # 透明度（0.9不透明）
        edgecolor='gray'           # 边框色（灰色）
    ))


plt.plot(x_line, y_line, color='red', linewidth=2, alpha=0.8)

plt.show()
total_points = len(y)  # 总点数
below_50_points = np.sum(y < 0.5)  # 50%概率以下的点数
below_ratio = below_50_points / total_points  

