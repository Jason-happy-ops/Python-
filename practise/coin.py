import random

times=0     #连续6次出现的总次数
experiments_with_streak = 0  #出现连续6次的实验次数
total_experiments = 10  #总实验次数

for experimentNumber in range(total_experiments):
    list_number=[]
    i=0
    while True:     #循环打印一个有x个随机数的列表
        a=random.randint(0,1)
        list_number.append(a)
        i+=1
        if i==100:
            break
    # 每次实验开始时重置连续正面计数
    numberOfStreaks = 0
    has_streak = False  #标记本次实验是否出现连续6次
    for num in list_number:
        if num==1:
            numberOfStreaks+=1
        else:
            numberOfStreaks=0
        if numberOfStreaks==6:
            times+=1
            has_streak = True  #标记本次实验出现了连续6次
    if has_streak:
        experiments_with_streak += 1

# 计算概率
probability = experiments_with_streak / total_experiments
print(f"本次进行了{total_experiments}次实验，每次抛掷{i}次")
print(f"连续6次正面出现的总次数: {times}次")
print(f"出现连续6次正面的实验次数: {experiments_with_streak}次")
print(f"连续6次正面的概率: {probability:.2%} ({experiments_with_streak}/{total_experiments})")


print(list_number)