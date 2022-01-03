import numpy as np
#(CBSE 2007-Question 3)
A2 = np.array([[3, 2], [2, 3]])
B2 = np.array([47,53])
x2 = np.linalg.solve(A2, B2) 
print(x2)