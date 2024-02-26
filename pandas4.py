import pandas as pd
s=pd.Series([10,20,30,40,10])
print(s)

# Sorting of series
print("Sorted series:")
print(s.sort_values())

# Unique values in series
print("Unique values are :",s.unique())

# Number of unique values in a series
print("Number of unique values are :",s.nunique())

# Summary of series statistics
print("Statistics summary of series :")
print(s.describe())