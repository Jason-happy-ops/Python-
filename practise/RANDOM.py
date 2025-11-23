import matplotlib.pyplot as plt
from random_run import Randomwalk

rw=Randomwalk()
rw.fill_work()
plt.style.use('classic')
fig,ax=plt.subplots()
ax.scatter(rw.x_value,rw.y_value,s=15)
ax.set_aspect('equal')
plt.show()
