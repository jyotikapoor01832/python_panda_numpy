import numpy as np
arr=np.array([[22,45,23,54,34],[34,54,45,65,23]])
print("Given array ")
print(arr)

print("Sorted array :")
print(np.sort(arr))

print("Shape of a given array :",np.shape(arr))

print("Location of an element in array :")
print(np.where(arr==65))