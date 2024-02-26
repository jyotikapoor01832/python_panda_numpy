# Find number of elements in a series
import pandas as pd
s = pd.Series([10,20,30,40,50])
print("Series is :",s)
print("Size of series is :",s.size)

# Finding average of element in a series
print("Mean is :",s.mean())

# Finding maximum value in a series
print("Maximum value is :",s.max())

# Finding minimum value in a series
print("Minimum value is :",s.min())