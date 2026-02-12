#利用pandas库处理csv文件数据
from _pytest.cacheprovider import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler ,MinMaxScaler  #归一化和标准化工具

class clean_data():
    def __init__(self,Path):
        self.path = Path
        self.df = pd.read_excel(self.path,na_values=[""])     #可以指定哪些值为空值



    def data_summary(self,core_cols):
        #输出行名，列名
        print("="*50)
        print(self.df.columns.tolist())
        print("="*50)
        print(self.df.index.tolist())


        #打印数据情况
        print(self.df.info())

        #查看缺失数量
        print(self.df.isnull().sum())

        #填充缺失值
        x = self.df[core_cols].mean()

        self.df = self.df.fillna(x,inplace=False)     # inplace=True直接修改原数据，False返回新数据
        self.df = self.df.dropna()

        #将某列转为数值列，errors='coerce'将非法值转为 NaN
        self.df[core_cols] = pd.to_numeric(self.df[core_cols], errors='coerce')

        #描述性统计
        print(self.df.describe())

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

    def data_process1(self,core_cols):
        #归一化
        scaler1 = MinMaxScaler()
        self.df[core_cols] = scaler1.fit_transform(self.df[[core_cols]])
        df_toexcel = self.df.copy()  # 复制数据以保存原始数据
        df_toexcel.to_excel(r"", index=False)       #不包含行索引


    def data_process2(self,core_cols,path):
        #标准化
        scaler2 = StandardScaler()
        self.df[core_cols] = scaler2.fit_transform(self.df[[core_cols]])   
        df_toexcel = self.df.copy()  # 复制数据以保存原始数据
        df_toexcel.to_excel(path, index=False)       #不包含行索引
        
    def data_process3(self,core_cols):    
        #分行的归一化
        groups = [(0,4),(5,12),(13,20)]  
        for start,end in groups:
            scaler1 = MinMaxScaler()
            self.df.loc[start:end,core_cols] = scaler1.fit_transform(self.df.loc[start:end,[core_cols]])


    def z_score_outlier(self,core_cols):
        #z-score判断异常值
        col = core_cols
        data = self.df[col].dropna()
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