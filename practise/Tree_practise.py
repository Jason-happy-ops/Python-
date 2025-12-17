from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeRegressor, export_graphviz
from sklearn.metrics import accuracy_score, confusion_matrix, r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

import pandas as pd
import openpyxl

path = pd.read_excel(r"C:\Users\29418\Desktop\python\practise\清理后数据.xlsx")

df = pd.DataFrame(path)


df.loc[:,"孕妇BMI"] = pd.to_numeric(df["孕妇BMI"], errors="coerce")       #X必须是二维数组
df.loc[:,"年龄"] = pd.to_numeric(df["年龄"], errors="coerce")
df.loc[:,"Y染色体浓度"] = pd.to_numeric(df["Y染色体浓度"], errors="coerce")     #Y必须是一维数组

# 去掉BMI、年龄或Y染色体浓度中存在缺失/非数值的数据行，避免模型训练报错
df = df.dropna(subset=["孕妇BMI", "年龄", "Y染色体浓度"])

BMI_data = df.loc[:,["孕妇BMI","年龄"]]
Y_nongdu = df.loc[:,"Y染色体浓度"]
X_train,X_test,Y_train,Y_test = train_test_split(BMI_data,Y_nongdu,test_size=0.2,random_state=42)     #这个随机种子是控制测试集训练集的
# 目标是连续值，使用回归树而不是分类树

grid_param = {'max_depth':[1,2,3,4,5],
'criterion':['squared_error','friedman_mse','absolute_error']}


grid_dt = GridSearchCV(DecisionTreeRegressor(random_state=42),grid_param,cv=5)          #这个随机种子是用来控制决策树训练过程的

grid_dt.fit(X_train,Y_train)         #用全部数据训练

new_sample = pd.DataFrame([[41.23, 30]],columns=['孕妇BMI','年龄'])
Y_pred = grid_dt.predict(new_sample)

Y_predict_test = grid_dt.predict(X_test)
R2 = r2_score(Y_test,Y_predict_test)

print(Y_pred)
print( f"决定系数(R2):{R2:2f}")
print(f"最优参数组合：{grid_dt.best_params_}")

