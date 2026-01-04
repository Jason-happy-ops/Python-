def length1(list):       #贪心算法求最大连续子数列，这种方法只能计算连续的递增最大长度
    global_length = 1       #记录全局最长子序列长度
    for i in range(len(list)):
        max_length = 1       #记录以list[i]为起点的最长子序列长度   
        last_num = list[i]      #记录当前最长子序列的最后一个数字

        for j in range(i+1,len(list)):
            if last_num < list[j]:
                max_length += 1
                last_num = list[j]
            global_length = max(global_length, max_length)  #更新全局最长子序列长度

    return global_length

def length2(list,n):       #暴力枚举+递归计算非连续递增最大长度
    if n >= len(list):
        return 0
    max_length = 1  # 初始化，至少包含自己
    for j in range(n + 1, len(list)):  # 从 n+1 开始，避免重复
        if list[j] > list[n]:
            current = 1 + length2(list, j)
            max_length = max(max_length, current)
    return max_length

# 全局最大长度函数
def length2_global(list):
    if not list:
        return 0
    return max(length2(list, i) for i in range(len(list)))


print(length2_global([5,1,2,4,3,6,7,1]))  # 全局: 5