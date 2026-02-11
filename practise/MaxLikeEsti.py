#最大似然估计
import numpy as np
from scipy.stats import norm , binom

#data应该是一维数组：list/np.array


#正态分布
estimated_mu, estimated_sigma = norm.fit(data)
print(f"MLE估计均值μ:{estimated_mu:.4f}")
print(f"MLE估计标准差σ:{estimated_sigma:.4f}")


#二项分布
# 方法1：已知n_trials，只估计p
# 用floc固定n，只估计p
estimated_p = binom.fit(data, floc=n_trials)[0]
print(f"已知试验次数n={n_trials}时,MLE估计的成功概率p:{estimated_p:.4f}")

# 方法2：n和p都未知，一起估计
estimated_n, estimated_p = binom.fit(data)
print(f"未知试验次数时,MLE估计的n:{estimated_n:.0f},p:{estimated_p:.4f}")







