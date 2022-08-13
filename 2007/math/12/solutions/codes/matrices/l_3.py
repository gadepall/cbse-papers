import numpy as np
A = np.array([[1, 2, -3], [3, 2, -2], [2, -1, 1]])
B = np.array([6,3, 2])
x = np.linalg.solve(A, B) 
print(x)