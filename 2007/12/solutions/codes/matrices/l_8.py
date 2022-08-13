import numpy as np
A1 = np.array([[27/45, -36/45], [36/45, 47/45]])
B1 = np.array([70,0])
xi = np.linalg.solve(A1, B1)
print(xi)