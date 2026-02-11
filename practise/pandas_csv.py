#利用pandas库处理csv文件数据
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Path = (r"")
df = pd.read_csv(Path)

#输出行名，列名
print("="*50)
print(df.columns.tolist())
print("="*50)
print(df.index.tolist())

#打印数据情况
print(df.info())

#查看缺失数量
print(df.isnull().sum())

#填充缺失值数量
df = df.fillna()
df = df.dropna()

#将某列转为数值列，errors='coerce'将非法值转为 NaN
df['列名'] = pd.to_numeric(df['列名'], errors='coerce')

#描述性统计
print(df.describe())

#z-score判断异常值
col = '关键列列名'
data = df[col].dropna()
mean = np.mean(data)
std = np.std(data,ddof=1)#样本标准差
z_scores = (data - mean) / std
#判断异常值
outliers = data[np.abs(z_scores) > 3]
cleaned_data = data[np.abs(z_scores) <= 3]
#异常值可视化
plt.boxplot(data, flierprops=dict(marker='o', color='red'))  # 箱线图，红点=异常值
plt.title(f"{col} 异常值可视化")
plt.show()