import matplotlib.pyplot as plt
x_values = [1,2,2.5,3,4,5]
y_values = [1,4,6.25,9,16,25]
fig,ax = plt.subplots()     #fig：生成图形  ax：绘图
ax.plot()      
ax.plot(x_values,y_values,linewidth=3)
ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Values",fontsize=14)
#刻度标记
ax.tick_params(labelsize=14)
plt.show()