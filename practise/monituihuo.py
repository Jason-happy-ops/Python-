import random
import math

#先初始化参数
x_start = 5
T = 40
a = 0.95
yuzhi = 0.001


def cal_energy(x):
    y = x**2 + 2*x
    return y

while True:
    
    if T <= yuzhi:
        print(round(x_new,4))
        break

    else :
        for i in range(200):
            x_new = x_start + random.uniform(-0.5,0.5)
            E_old = cal_energy(x_start)
            E_new = cal_energy(x_new)
            E_minus = E_new - E_old
            if E_minus <= 0:
                x_start = x_new
            #这是模拟退火的核心，他需要进行这样一个概率的比较！
            if E_minus > 0:
                accept_prob = math.exp(-E_minus / T)
                random_p = random.random()
                if accept_prob > random_p:
                    x_start = x_new
        T = T*a