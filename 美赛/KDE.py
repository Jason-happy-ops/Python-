import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_excel(r"C:\Users\29418\Desktop\Problem1.xlsx")

def KDE_plot(name):

    name = name.dropna()
    #高斯核，以及计算X,Y轴值

    kernel = stats.gaussian_kde(name)  # 高斯核（默认，最常用）
    x_range = np.linspace(name.min()-0.05, name .max()+0.05, 1000)  # 生成x轴连续值
    y_kde = kernel(x_range)  # 计算每个x对应的核密度值
    plt.figure(figsize=(10, 6))
    plt.plot(x_range, y_kde, color="#0691CD", lw=2, label='KDE Curve')
    plt.fill_between(x_range, y_kde, color="#6DBFE1", alpha=0.3)

    plt.title('Kernel Density Estimation (KDE) of ' + name.name + ' Percentages', fontsize=16)
    plt.xlabel(name.name + ' Percentage', fontsize=14)
    plt.ylabel('Density', fontsize=14)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    KDE_plot(df['judge_pct'])
    KDE_plot(df['median'])
    KDE_plot(df['deviation'])
    KDE_plot(df['average'])