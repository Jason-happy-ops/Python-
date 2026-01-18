import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split , GridSearchCV
from sklearn.metrics import accuracy_score, roc_auc_score

df = pd.read_csv(r"C:\Users\29418\Desktop\美赛\2024_MCM_Problem_C_Data\2024_Wimbledon_featured_matches.csv")

# 向量化生成新列
df['is_increase'] = 0  # 先默认设为0

# 条件1：下一行p1_score > 当前行p1_score
cond1 = df['p1_score'].shift(-1) > df['p1_score']

# 条件2：当前行p1_score == 'AD'（表示player1获胜）
cond2 = df['p1_score'] == 'AD'

# 满足任一条件则设为1
df['is_increase'] = (cond1 | cond2).astype(int)

#GBDT梯度提升树
df2 = pd.read_csv(r"C:\Users\29418\Desktop\美赛\processed_data.csv")


