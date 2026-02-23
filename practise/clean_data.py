#利用pandas库处理csv文件数据
from _pytest.cacheprovider import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler ,MinMaxScaler  #归一化和标准化工具
import seaborn as sns

class clean_data():
    def __init__(self,Path):
        self.path = Path
        self.df = pd.read_excel(self.path,na_values=[""])     #可以指定哪些值为空值



    def data_summary(self,core_cols=None):
        #输出行名，列名
        a = input("是否查看行列名 0:no 1:yes:")
        if a=="1":
            print("="*50)
            print(self.df.columns.tolist())
            print("="*50)
            print(self.df.index.tolist())


        #打印数据情况
        print(self.df.info())

        #查看缺失数量
        print(self.df.isnull().sum())

        #填充缺失值
        c = input("是否填充缺失值 0:no 1:yes:")

        if c=="1":

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


    def spearman_outlier(self,core_cols):
        #斯皮尔曼系数
        spearman_correlation = self.df[core_cols].corr(method='spearman')
        print("斯皮尔曼相关系数：")
        print(spearman_correlation)

    def matrix(self,core_cols):
        #相关矩阵
        correlation_matrix = self.df[core_cols].corr()
        print("相关矩阵：")
        print(correlation_matrix)

    def correlation_heatmap(self,core_cols):
        #相关性热图
        plt.figure(figsize=(10,8))
        sns.heatmap(self.df[core_cols].corr(),cmap="#5DCF2C",annot=True #显示数值
                   ,robust=True)