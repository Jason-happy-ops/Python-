import numpy as np
import pandas as pd
import random

company = ["A","B","C"]
df = pd.DataFrame({"company":[company[x] for x in np.random.randint(0,3,10)],
                  "salary":np.random.randint(30,70,10),
                    "age":np.random.randint(20,50,10)
                    })

group = df.groupby("company") .agg({"salary":"mean","age":"mean"})  
print(list(group))