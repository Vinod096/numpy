import numpy as np

x = np.arange(20).reshape(4,5)
print("x array : \n", x)

print("z diag_array : \n", np.diag(x))

print("y diag_array : \n", np.diag(x, k=1))

print("w array : \n", np.diag(x, k=-1))