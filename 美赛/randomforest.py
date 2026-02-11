import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, export_graphviz
from sklearn.metrics import accuracy_score, confusion_matrix, r2_score
from sklearn.model_selection import GridSearchCV


df = pd.read_excel(r"C:\Users\29418\Desktop\Problem1(1).xlsx")
#用两个随机森林，特征列一样，目标列为评委评分和粉丝评分


#X特征列转为二维数组
df.loc[:,"ballroom_partner"] = pd.to_numeric(df["ballroom_partner"], errors="coerce")
df.loc[:,"celebrity_age_during_season"] = pd.to_numeric(df["celebrity_age_during_season"], errors="coerce")
df.loc[:, "celebrity_industry"] = pd.to_numeric(df["celebrity_industry"], errors="coerce")
df.loc[:,"week"] = pd.to_numeric(df["week"],errors="coerce")

#Y目标列
df.loc[:,"judge_pct"] = pd.to_numeric(df["judge_pct"], errors="coerce")

value1 = df.loc[:,["ballroom_partner","celebrity_industry","week"]]
value2 = df.loc[:,['week','judge_pct','celebrity_industry']]

judge_score = df.loc[:,"judge_pct"]
fan_score = df.loc[:,"median"]

X_train1,X_test1,Y_train1,Y_test1 = train_test_split(value1,judge_score,test_size=0.2,random_state=42)
X_train2,X_test2,Y_train2,Y_test2 = train_test_split(value2,fan_score,test_size=0.2,random_state=42)


grid_param = {'max_depth':[5,8,11],#特征较多防止欠拟合
'criterion':['squared_error','friedman_mse','absolute_error'],'min_samples_split':[2,5,10]}
 
 #这个随机种子是用来控制决策树训练过程的
grid_dt_judge = GridSearchCV(RandomForestRegressor(n_estimators=200,random_state=42),grid_param,cv=5)            


grid_dt_judge.fit(X_train1,Y_train1)         #用全部数据训练



Y_predict_test = grid_dt_judge.predict(X_test1)
R2 = r2_score(Y_test1,Y_predict_test)

print("-"*50)
print( f"评委决定系数(R2):{R2:2f}")
print(f"评委最优参数组合：{grid_dt_judge.best_params_}")


grid_dt_fan = GridSearchCV(RandomForestRegressor(n_estimators=200,random_state=42),grid_param,cv=5)            
grid_dt_fan.fit(X_train2,Y_train2)


Y_predict_test_fan = grid_dt_fan.predict(X_test2)
R2_fan = r2_score(Y_test2,Y_predict_test_fan)

print("-"*50)
print( f"粉丝决定系数(R2):{R2_fan:2f}")
print(f"粉丝最优参数组合：{grid_dt_fan.best_params_}")


pass
# 训练完评委分模型后，输出特征作用
best_rf_judge = grid_dt_judge.best_estimator_
judge_importance = pd.Series(
    best_rf_judge.feature_importances_,
    index=["ballroom_partner","celebrity_industry","week"]
)
print("=== 每个特征对评委分的作用占比 ===")
print(judge_importance * 100)  # 转成百分比更直观

# 训练完粉丝投票模型后，同理
best_rf_vote = grid_dt_fan.best_estimator_
vote_importance = pd.Series(
    best_rf_vote.feature_importances_,
    index=['week','judge_pct','celebrity_industry'])
print("=== 每个特征对粉丝投票的作用占比 ===")
print(vote_importance * 100)

