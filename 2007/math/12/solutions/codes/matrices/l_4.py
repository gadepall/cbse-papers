import numpy as np
import mpmath as mp
A = np.array([2, -2, 1]) 
B=np.array([1, 2, -2])
C =np.array([2, -1, 4])
p=(B+C).T@A/mp.sqrt(A.T@A)
print(p)