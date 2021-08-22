import numpy as np

x = np.arange(25).reshape(5,5)
print("The elements in x that are greater than 10 : ",x[x>10] )
print("The elements in x that are less than equal to 7 : ", x[x<=7])
print("The elements in x that are between 10 & 17 :", x[(x>10)&(x<17)])
x[(x>10)&(x<17)] = -1
print('x : \n',x)