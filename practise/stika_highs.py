from pathlib import Path
import csv

path = Path(r"C:\Users\29418\Desktop\python\practise\weather_data\sitka_weather_07-2021_simple.csv")
lines = path.read_text().splitlines()   #链式调用获取一个包含文件中各行的列表

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

