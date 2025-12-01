from pathlib import Path
import json
import plotly.express as px
import pandas as pd


path = Path(r"C:\Users\29418\Desktop\python\practise\eq_data\eq_data_30_day_m1.geojson")
try:
    contents = path.read_text()

except:
    contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)      #转换为python对象

all_eq_dicts = all_eq_data['features']      #相当于形成了一个列表
print(len(all_eq_dicts))
mags,titles,lons,lats=[],[],[],[]

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']      #相当于有一个大字典eq_dict,它有一个键properties,properties又是一个字典存储了mag键
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

#循环完之后在封装数据
data = pd.DataFrame(data=zip(lons,lats,titles,mags),columns=['经度','纬度','位置','震级'])

fig = px.scatter(data,x='经度',y='纬度',
range_x=[-200,200],range_y=[-90,90],width=800,height=800,title='全球地震散点图',
size='震级',size_max=10,color='震级',hover_name='位置')

fig.write_html('global_earthquakes.html')
fig.show()




path = Path('practise/eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data,indent=4)        #指定缩进量
path.write_text(readable_contents)

