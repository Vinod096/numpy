import numpy as np

x = np.arange(20).reshape(4,5)
print("X_Array : \n", x)

z = x[1:4, 2:5]

print("z Array : \n",z)

w = x[1:, 2:5]
print("w Array : \n", w)

y = x[:3, 2:5]
print("y array : \n",y)
