import numpy as np
#(CBSE 2007-Question 2)
A1 = np.array([[1, 6], [3, -8]])
B1 = np.array([6,5])
xi = np.linalg.solve(A1, B1) 
x=xi[0]
y=1/xi[1]
x1= np.array([x,y])
print(x1)


