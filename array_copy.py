import numpy as np
x = np.arange(20).reshape(4,5)
print("X : \n",x)
z = np.copy(x[1:4,2:5])
print("z array : \n",z)
w = x[1:4,2:5].copy()
print("w array:\n",w)
z[2,2] = 55
w[2,2] = 44
print("x : \n",x)
print("z :\n",z)
print("w : \n",w)