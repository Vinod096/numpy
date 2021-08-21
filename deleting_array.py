import numpy as np

x = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("Original x = ",x)

delete_array = np.delete(x, 0 ,axis = 0)

print(" New _array : ", delete_array)

deleted_array_2 = np.delete(x,[0,2], axis = 1)

print("New array 2 : \n",deleted_array_2)