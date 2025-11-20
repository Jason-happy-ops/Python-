import matplotlib.pyplot as plt
import numpy as np

years=[
    '2021Q1','2021Q2','2021Q3','2021Q4',
    '2022Q1','2022Q2','2022Q3','2022Q4',
    '2023Q1','2023Q2','2023Q3','2023Q4',
    '2024Q1','2024Q2','2024Q3','2024Q4',
    '2025Q1','2025Q2','2025Q3'
    ]



us_data=[1000,400,360,1402.2,1340,414,182,694,600,350,330,1000,500,300,435,979,600,250,50]       #美国
br_data=[1163,939,679,1199,1200,1400,1000,1840,1200,2000,1800,1996,1500,2100,1600,2265,1454,2772,3184]     #巴西
ag_data=[105,90,60,120,85,110,60,110,65,40,25,70,40,35,75,260,15,30,120]           #阿根廷

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['axes.linewidth']=1.2
plt.rcParams['grid.linewidth']=0.8
plt.rcParams['legend.framealpha']=0.9

plt.rcParams['font.size']=11
fig,ax=plt.subplots(figsize=(12,7))
line1,=ax.plot(years,us_data,label='US',marker='o',linewidth=2,markersize=6)
line2,=ax.plot(years,br_data,label='Brazil',marker='*',linewidth=2,markersize=6)
line3,=ax.plot(years,ag_data,label="Agintina",marker='^',linewidth=2,markersize=6)
for x,val in zip(years,us_data):
    ax.text(x,val,f"{val}",ha='center',va='bottom',fontsize=8,color=line1.get_color())
for x,val in zip(years,br_data):
    ax.text(x,val,f"{val}",ha='center',va='bottom',fontsize=8,color=line2.get_color())
for x,val in zip(years,ag_data):
    ax.text(x,val,f"{val}",ha='center',va='bottom',fontsize=8,color=line3.get_color())

ax.set_xlabel('Year',fontsize=13,fontweight='bold')
ax.set_ylabel('Export to China/tons',fontsize=13,color='black')
ax.grid(linestyle='--',alpha=0.6)

plt.title('soybeans to China',fontweight='bold')
plt.tight_layout()
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years, rotation=45)

ax.legend(loc='upper left') #标明放在图表左上角

plt.show()
