import pandas as pd
name = pd.Series(["Rohit","Virat"])
team = pd.Series(["MI","RCB"])
dic = {'Name':name,'Team':team}
df = pd.DataFrame(dic)
print(df)
