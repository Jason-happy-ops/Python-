from GBDT_data import df2
import numpy as np
import pandas as pd
import math


seq = df2["is_increase"].values
    
    # 2. 统计0和1的数量（后续计算期望游程数用）
n1 = (seq == 1).sum()  # 1的个数
n2 = (seq == 0).sum()  # 0的个数
total = len(seq)


R=1   
for i in range(1, total):
            
    if seq[i] != seq[i-1]:
                R += 1



def runs_test(n1, n2, R):
    """
    计算游程检验的期望游程数、标准差和Z分数
    :param n1: 类别1的样本数
    :param n2: 类别2的样本数
    :param R: 实际游程数
    :return: (期望游程数μR, 标准差σR, Z分数Z)
    """
    # 计算期望游程数 μR
    mu_R = (2 * n1 * n2) / (n1 + n2) + 1
    
    # 计算游程数的标准差 σR
    numerator = 2 * n1 * n2 * (2 * n1 * n2 - n1 - n2)
    denominator = (n1 + n2) ** 2 * (n1 + n2 - 1)
    sigma_R = math.sqrt(numerator / denominator)
    
    # 计算Z分数
    Z = (R - mu_R) / sigma_R
    
    return mu_R, sigma_R, Z

# 示例：代入数值计算
if __name__ == "__main__":
    
    n1 = (seq == 1).sum()  # 1的个数
    n2  = (seq == 0).sum()  # 0的个数



    R=1   
    for i in range(1, total):
            
        if seq[i] != seq[i-1]:
                R += 1
    
    mu_R, sigma_R, Z = runs_test(n1, n2, R)
    print(f"期望游程数 μR: {mu_R:.4f}")
    print(f"游程数标准差 OR: {sigma_R:.4f}")
    print(f"Z分数 Z: {Z:.4f}")