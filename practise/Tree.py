#鸢尾花预测
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

iris = load_iris()          #本身自带150个样本
X = iris.data       #4个花的特征
Y = iris.target     #3类鸢尾花


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
dt = DecisionTreeClassifier(criterion='gini',max_depth=3,random_state=42)

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
