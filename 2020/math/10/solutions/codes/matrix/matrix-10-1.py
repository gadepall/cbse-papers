import numpy as np

m = 2
n =3 

#Given points
A = np.array(([m,-n]))
B = np.array(([-m,n]))

#Distance between A and B
d = np.linalg.norm(A-B)

print(d,d**2)
