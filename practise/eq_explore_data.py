from pathlib import Path
import json

path = Path(r"C:\Users\29418\Desktop\python\practise\eq_data\eq_data_1_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)      #转换为python对象

path = Path('practise/eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data,indent=4)        #指定缩进量
path.write_text(readable_contents)

