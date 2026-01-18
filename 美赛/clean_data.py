#利用pandas库处理csv文件数据
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Path = (r"C:\Users\29418\Desktop\美赛\2024_MCM_Problem_C_Data\2024_Wimbledon_featured_matches.csv")
df = pd.read_csv(Path)

#输出行名，列名
print("="*50)
print(df.columns.tolist())
#print("="*50)
#print(df.index.tolist())

print("="*50)
#打印数据情况
print(df.info())

print("="*50)
#查看缺失数量
print(df.isnull().sum())

#填充缺失值数量
#df = df.fillna()
#df = df.dropna()

#将某列转为数值列，errors='coerce'将非法值转为 NaN
#df['列名'] = pd.to_numeric(df['列名'], errors='coerce')

#描述性统计
print(df.describe())