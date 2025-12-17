from tkinter import Grid
import tabulate
data_dict = {
    "Names": ["Judy", "Lucy", "Paul", "Jason"],
    "Age": ["22", "43", "37", "18"],
    "Lan": ["C", "Java", "C++", "Python"]
}

# 关键：指定 headers="keys"，告诉 tabulate 用字典的键作为表头
# 同时用 *zip(*data_dict.values()) 把“列数据”转成“行数据”
table_1 = tabulate.tabulate(zip(*data_dict.values()), headers=data_dict.keys(), tablefmt="grid")
print(table_1)

