import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler


df = pd.read_excel(r"C:\Users\29418\Desktop\python\美赛\2026_MCM_Problem_C_Data (1).xlsx")
df.replace("N/A",np.nan,regex=False,inplace=False).to_excel(r"C:\Users\29418\Desktop\python\美赛\2026_MCM_Problem_C_Data (1).xlsx",index=False)

def data_process1(core_cols):
    #归一化
    scaler1 = MinMaxScaler()
    df[core_cols] = scaler1.fit_transform(df[core_cols])
    df_toexcel = df.copy()  # 复制数据以保存原始数据
    return df_toexcel
        


def data_process2(core_cols):
    #标准化
    scaler2 = StandardScaler()
    df[core_cols] = scaler2.fit_transform(df[core_cols])   
    df_toexcel = df.copy()  # 复制数据以保存原始数据
    return df_toexcel


a = input("是否查询数据总览?y/n")
if a == "y":
    print(df.describe())
    print(df.info())

print(df.groupby("season").apply(lambda x:data_process1(x.iloc[:,8:-1].columns.tolist())).head())
