import pandas as pd
s = pd.Series([10,20,30,40])
df = pd.DataFrame(s)

# Rename a column in a dataframe
df.columns = ['list1']

# Creating a new column
df['list2'] = 20
print("Creating a new column :\n", df)

# Adding 2 columns and make another column
df['list3'] = df['list1'] + df['list2']
print("Adding 2 columns and make another column :\n",df)

# Delete a column from dataframe
df.pop('list2')
print("Deleting a column using pop :\n",df)

# Drop() for deleting rows and columns
df1 = df.drop(index = 2,axis =0)
print("Drop rows having index 2 :\n",df1)