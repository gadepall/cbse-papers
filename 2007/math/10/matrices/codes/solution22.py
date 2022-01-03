
import numpy as np
#(CBSE 2007-Question 22)
n= np.array([1,-1])
A3= np.array([3,-1])
B3= np.array([8,9])
c=2
k= (c-A3.T@n)/(B3.T@n-c)
print(k)