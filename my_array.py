import numpy as np

y = np.load('my_array_file.npy')
print (y)
print('y = ',y)
print()

print('y is an object of type :', type(y))
print('The elements in y are of type : ', y.dtype)