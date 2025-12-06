from tkinter import Y
import cleandata
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 替换原字体配置行（第7-8行）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

Y_nongdu = cleandata.df1["Y染色体浓度"]
BMI_data = cleandata.df1["孕妇BMI"]




key_week_nums = []

fig,(ax1,ax2) = plt.subplots(nrows=1,ncols=2,figsize=(10,4))
#Y浓度和BMI关系
ax1.scatter(BMI_data,Y_nongdu,c=Y_nongdu,cmap=plt.cm.Blues,s=20)

ax1.set_title("Relationship between Y and BMI")
def transform(str_days):
    # 处理空值或NaN
    if pd.isna(str_days) or str(str_days).strip() == '':
        return np.nan
    
    str_days = str(str_days).strip()
    # 统一转换为小写，并处理加号
    temp_str = str_days.upper().replace("W", ",").replace("+", "")
    
    # 如果只有周数（如 "16W"），split后只有一个元素
    parts = temp_str.split(",")
    
    try:
        week_num = int(parts[0])
        # 如果只有周数没有天数，day_part为空，默认为0
        day_num = int(parts[1]) if len(parts) > 1 and parts[1].strip() != '' else 0
        total_days = week_num*7+day_num
        return total_days
    except (ValueError, IndexError) as e:
        # 如果解析失败，返回NaN
        print(f"无法解析格式: {str_days}, 错误: {e}")
        return np.nan


cleandata.df1["总天数"]=cleandata.df1["检测孕周"].apply(transform)#不用再加（）了pandas会自己调用函数检测每一列


GA_yunzhou = cleandata.df1["总天数"]


#GA和Y浓度关系
ax2.scatter(GA_yunzhou,Y_nongdu,c=Y_nongdu,cmap=plt.cm.Reds,s=20)

ax2.set_title("Relationship between Y and GA")
ax2.set_ylabel("Y浓度",fontsize=10)
ax2.set_xlabel("GA/Days",fontsize=10)



fig.savefig("question1", dpi=300, bbox_inches="tight")  # 用fig.savefig()
plt.show()