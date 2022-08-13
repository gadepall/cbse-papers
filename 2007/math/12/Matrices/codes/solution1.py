import numpy as np
#(CBSE 2007-Question 1)
A = np.array([[2, -3], [3, 4]])
I= np.array([[1, 0], [0, 1]])
print((np.matmul(A,A))-(6*A)+(17*I))
print(np.linalg.inv(A))