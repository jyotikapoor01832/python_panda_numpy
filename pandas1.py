# Woorking with series in pandas
import pandas as pd
s = pd.Series([10,20,30,40])
print(s)
print(s[1])

# Giving index to the series
s1=pd.Series([11,22,33,44],index=['a','b','c','d'])
print(s1)
print(s1['c'])

# Adding 3 to each value of s array
print(s+3)

#Getting values greater than 22
s2=s1[s1>22]
print(s2)