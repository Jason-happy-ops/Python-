from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

path = Path(r"C:\Users\29418\Desktop\python\practise\weather_data\sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()   #链式调用获取一个包含文件中各行的列表



reader = csv.DictReader(lines)          #把csv文件的文本行(lines)转成可以调用的容器————字典
header_row = next(reader)           #只调用了一次文件头，所以获得的是第一行的内容
dates,highs,lows=[],[],[]
for row in reader :
    current_date = datetime.strptime(row['DATE'],'%Y-%m-%d')
    try:
        high = int(row['TMAX'])      #把文本格式处理成数值格式
        low = int(row['TMIN'])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)


plt.style.use('ggplot')
fig,ax = plt.subplots()
ax.plot(dates,highs,color='red',alpha=0.5)
ax.plot(dates,lows,color='blue',alpha=0.5)

ax.set_title("Daily High and Low Temperatures",fontsize=24)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)",fontsize=16)
ax.tick_params(labelsize=16)

plt.show()