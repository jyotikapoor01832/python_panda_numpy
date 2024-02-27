import pandas as pd
dic1 = {"name" :["Sachin","Nitin","Pandya"],"age":[30,35,32]}
df = pd.DataFrame(dic1)
# Boolean indexing in dataframe
df.index=[True,False,True]
print("After indexing :\n", df)
# Show the dataframe where index = True
print(" Show rows where index = True :\n ",df.loc[True])

#Concatenate DataFrames
dic2 = {"name":["Ridhi","Sidhi","Nidhi"],"age":[20,30,25]}
df1 = pd.DataFrame(dic2)
print("\nSecond dataframe :\n",df1)

df2 = pd.concat([df,df1])
print("After concatenate :\n",df2)
