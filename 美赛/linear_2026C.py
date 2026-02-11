#检验显著性

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

path = r"C:\Users\29418\Desktop\Problem1(1).xlsx"
df = pd.read_excel(path)

print("查看所有列名：",df.columns.tolist())

feature_cols = ["celebrity_age_during_season","ballroom_partner","celebrity_industry","week"]

X = df[feature_cols]

Y = df["judge_pct"]

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

features_xianzhu = sm.add_constant(X)
Linearmodel = sm.OLS(Y,features_xianzhu).fit()
print('显著性检验')
print(Linearmodel.summary())