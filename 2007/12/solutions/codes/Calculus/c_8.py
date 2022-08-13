import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0, '/Users/Priyanka/Desktop/courses/pythonandlatex/2007/10/solutions/codes/CoordGeo')   

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen




def f(x,k):
    if (x <=1):
        fval = k*x**2 
        return fval
    else:
        return 4

fvec = np.vectorize(f)
x = np.linspace(-1,3,100)




##Input parameters
k = 3
#
plt.plot(x,fvec(x,k),label='discontinuous, k = 3')
k = 4
plt.plot(x,fvec(x,k),label='continuous, k = 4')
#
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
#plt.axis('equal')


plt.show()