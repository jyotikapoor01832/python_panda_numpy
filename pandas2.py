# Working with series in Pandas along with Numpy
import pandas as pd
import numpy as np

arr=np.array([10,20,30,40,50])
index = np.array(['a','b','c','d','e'])
s = pd.Series(arr,index=index)
print(s)