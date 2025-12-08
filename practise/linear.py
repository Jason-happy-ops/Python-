import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

path = r"C:\Users\29418\Desktop\python\practise\清理后数据.xlsx"
df = pd.read_excel(path)

print("查看所有列名：",df.columns.tolist())

feature_cols = ["孕妇BMI","孕周_总天数","年龄"]

X = df[feature_cols]

Y = df["Y染色体浓度"]

model = LinearRegression()
model.fit(X,Y)

coef_df = pd.DataFrame({
    "特征列名": feature_cols,
    "特征系数(β)": model.coef_
})
print("\n=== 列名-系数对照表 ===")
print(coef_df)
print(f"截距{model.intercept_:.2f}")

r2 = model.score(X , Y)
print(f"决定系数：{r2:.4f}")