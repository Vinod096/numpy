import numpy as np
x = np.array([1,2,3,4])
x = np.append(x,6)
print("X_Original_Array : ", x)

y = np.array([[1, 2, 3], [4, 5, 6]])
print("Y_Original_Array : ", y)
new_y = np.append(y, [[7,8,9]], axis = 0)
print("New Y array : ",new_y)
Appened_y_array = np.append(y, [[9], [10]], axis=1)
print("Appended Y : ",Appened_y_array)
