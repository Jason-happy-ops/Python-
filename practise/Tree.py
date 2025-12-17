#鸢尾花预测
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import GridSearchCV

iris = load_iris()          #本身自带150个样本
X = iris.data       #4个花的特征
Y = iris.target     #3类鸢尾花


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)     #这个随机种子是控制测试集训练集的
dt = DecisionTreeClassifier(criterion='gini',max_depth=3,random_state=11)               #这个随机种子是用来控制决策树训练过程的

dt.fit(X_train,Y_train)         #用全部数据训练

new_sample = [[5.1,4.5,1.4,0.3]]
pred = dt.predict(new_sample)

print("预测结果：",pred[0])
print("预测的鸢尾花种类:",iris.target_names[pred[0]])

plt.figure(figsize=(12,8))
plot_tree(dt,
    feature_names=iris.feature_names,  # 显示特征名
    class_names=iris.target_names,     # 显示类别名
    filled=True,                      
    rounded=True,                     
    fontsize=10 )
plt.show()

y_pred = dt.predict(X_test)         #喂测试集特征，输出Y,根据测试集特征计算得到的“考试结果”，和“考试答案”Y_test不一样

accuracy = accuracy_score(Y_test,y_pred)

conf_mat = confusion_matrix(Y_test,y_pred)

print(f"测试集准确率：{accuracy:.2f}(越接近1越好)")
print("\n混淆矩阵(行=真实类别，列=预测类别):")
print(conf_mat)
print("类别对应:0=setosa, 1=versicolor, 2=virginica")

feature_importance = dt.feature_importances_

feature_names = iris.feature_names
importance_dict = dict(zip(feature_names, feature_importance))

for feat, imp in importance_dict.items():
    print(f"{feat:15} → {imp:.3f}")


#网格搜索，自动选择交叉系数最高的选项
##   打印DecisionTreeClassifier的默认参数
##   print(DecisionTreeClassifier().get_params())

param_grid = {'max_depth':[1,2,3,4,5],
'criterion':['gini','entropy'],
'min_samples_leaf':[3,5,7]}
grid = GridSearchCV(DecisionTreeClassifier(random_state=42), 
                    param_grid, cv=5)


grid.fit(X_train,Y_train)
print(f"最优参数组合：{grid.best_params_}")
print(f"最优参数下的交叉验证分数：{grid.best_score_:.3f}")