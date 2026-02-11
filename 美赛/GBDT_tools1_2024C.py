import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, log_loss


from GBDT_data import df2


def train_gbdt_model():
    feature_cols = ["p1_sets","p2_sets","p1_games","p2_games","server"]

    X = df2[feature_cols]
    y = df2["is_increase"]                        

    #划分训练集/测试集（固定7:3比例，保证结果可复现）
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

        
        
    gbdt = GradientBoostingClassifier(
    learning_rate=0.2,    # 文档最优值
    max_depth=5,          # 文档最优值
    n_estimators=300,     # 文档最优值
    random_state=42,      # 固定种子，结果可复现
    loss="log_loss"       # 二分类概率预测必需损失函数
            )

# 训练模型（仅1行核心代码）
    gbdt.fit(X_train, y_train)

# -------------------------- 3. 输出概率结果与基础评估--------------------------
# 1. 预测概率（核心输出：每行对应1个样本，[负类概率，正类概率]）
    train_prob = gbdt.predict_proba(X_train)  # 训练集概率
    test_prob = gbdt.predict_proba(X_test)    # 测试集概率

    all_win_prob = gbdt.predict_proba(X)[:, 1]  # 所有样本的赢的概率

    return all_win_prob


if __name__ == "__main__":
    result = train_gbdt_model()
    print(result)