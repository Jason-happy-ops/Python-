from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path(r"C:\Users\29418\Desktop\python\practise\weather_data\sitka_weather_07-2021_simple.csv")
lines = path.read_text().splitlines()   #链式调用获取一个包含文件中各行的列表



reader = csv.reader(lines)          #把csv文件的文本行(lines)转成可以调用的容器
header_row = next(reader)
dates,highs=[],[]
for row in reader :
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    high = int(row[4])      #把文本格式处理成数值格式
    dates.append(current_date)
    highs.append(high)


plt.style.use('ggplot')
fig,ax = plt.subplots()
ax.plot(dates,highs,color='red')

ax.set_title("Daily High Temperature,July 2021",fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)",fontsize=16)
ax.tick_params(labelsize=16)

plt.show()