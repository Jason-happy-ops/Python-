import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Path = (r"C:\Users\29418\Desktop\important.xlsx")
df = pd.read_excel(Path)

# 把所有单元格里的N/A替换成 0
df = df.replace("N/A", 0)

#计算职业个数
target_series = "celebrity_industry"
count = df[target_series].value_counts().reindex(range(1, 9), fill_value=0)

for num, cnt in count.items():
    print(f"{num}: {cnt}")


df.to_excel(Path, index=False)

#把获得前三名的小组单独拿出来
target_cols = "results"
df_top3 = df[df[target_cols].isin([1, 2, 3])]

try:
    new_excel_path = "C:/Users/29418/Desktop/top_3_groups.xlsx"
    df_top3.to_excel(new_excel_path, index=False)
except:
    print("Error: Unable to save the top 3 groups to Excel.")