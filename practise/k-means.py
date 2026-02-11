import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import indices, random
from sklearn.cluster import KMeans  
import pandas as pd

#全局变量 data
global data

# 设立随机种子
np.random.seed(42)

#导入数据
data = #尽量二维数据
#肘部法则先生成K值

import matplotlib.pyplot as plt

# 计算不同K值的误差平方和（SSE）
sse = []
for k in range(1, 6):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
    kmeans.fit(data)
    sse.append(kmeans.inertia_)  # inertia_是SSE：样本到其质心的距离平方和

# 绘制肘部图
plt.plot(range(1, 6), sse, marker='o')
plt.xlabel('Kvalue')
plt.ylabel('SSE')
plt.title('decide K ')
plt.show()



def SA():
    k = 3
    indices = np.random.choice(len(data), size=k, replace=False)#随机选k个做为初始聚类中心的索引
    centers = data[indices].copy()  # 直接切片，更高效
    def cal_energy(centers):        #算所有点的能量大小
        energy = 0
        for point in data:
            dists = [np.linalg.norm(point - center) for center in centers]
            energy += min(dists)**2
        return energy
    #初始化参数
    x_start = centers
    T = 40
    a = 0.95
    yuzhi = 0.001

    while True:
    
        if T <= yuzhi:
            best_centers = [[round(c[0],3), round(c[1],3)] for c in centers]
            print(best_centers)
            break

        else :
            for i in range(200):
                new_centers = [c.copy() for c in x_start]
                idx = random.randint(0, k)
                new_centers[idx][0] += random.uniform(-0.5,0.5)
                new_centers[idx][1] += random.uniform(-0.5,0.5)

                E_old = cal_energy(x_start)
                E_new = cal_energy(new_centers)
                E_minus = E_new - E_old
                if E_minus <= 0:
                    x_start = new_centers       

                if E_minus > 0: 
                    accept_prob = math.exp(-E_minus / T)
                    random_p = random.random()
                    if accept_prob > random_p:
                        x_start = new_centers

            T = T*a

    return x_start      




x_start_result = SA()
print("模拟退火算法得到的聚类中心：", x_start_result)






kmeans = KMeans(n_clusters=3, #聚类个数
                n_init=1,
                init=np.array(x_start_result), #使用模拟退火得到的聚类中心初始化 
                random_state=42)

kmeans.fit(data)        #训练后把训练数据存到kmeans中
#每个样本的聚类标签
labels = kmeans.labels_
print("样本聚类标签：", labels)  

#聚类中心（质心）
centers = kmeans.cluster_centers_
print("聚类中心：\n", centers) 

#预测新样本的标签
new_data = 
pred_labels = kmeans.predict(new_data)
print("新样本预测标签：", pred_labels) 