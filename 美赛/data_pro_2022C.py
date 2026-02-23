import pandas as pd
import time
import sys 
import os
# 1. 定义基础路径（你存放clean_data.py的根文件夹）
base_dir = r"C:\Users\29418\Desktop\python"
# 2. 拼接出目标文件夹的绝对路径（放clean_data.py的文件夹）
target_dir = os.path.join(base_dir, "practise")  # 结果：C:\Users\29418\Desktop\python\practise

# 3. 把目标文件夹加入Python搜索路径
sys.path.append(target_dir)

print("clean_data.py是否存在:", os.path.exists(os.path.join(target_dir, "clean_data.py")))

from clean_data import clean_data




#黄金
df1 = pd.read_excel(r)
#比特币
df2 = pd.read_excel(r)

df = pd.merge(df1,df2,on="Date",how = "outer")

#格式化时间并排序
df["Date"] = pd.to_datetime(df["Date"])

df = df.sort_values("Date")



df.to_excel(r"C:\Users\29418\Desktop\prediction.xlsx",index=False)
df = pd.read_excel(r"C:\Users\29418\Desktop\prediction.xlsx")

data_info = clean_data(r"C:\Users\29418\Desktop\prediction.xlsx")

data_info.data_summary()