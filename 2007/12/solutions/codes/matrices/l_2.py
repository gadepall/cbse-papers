import numpy as np
a= 3
b=4
c=5
A =np.array([[a-b-c,2*a ,2*a],[2*b,b-c-a,2*b],[2*c,2*c,c-b-a]])
d1=(np.linalg.det(A))
e= (a+b+c)**3
d= int(d1)
if(d==e):
    print(1)
else:
    print(0)    