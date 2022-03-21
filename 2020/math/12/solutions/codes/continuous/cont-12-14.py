#Code by GVV Sharma (works on termux)
#March 19, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the value of k for which the function is continuous


#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0,'/storage/emulated/0/github/cbse-papers/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if


def f(x,k):
    if (x <=1):
        fval = k*x**2 + 5
        return fval
    else:
        return 2

fvec = np.vectorize(f)
x = np.linspace(-1,3,100)




##Input parameters
k = -2
#
plt.plot(x,fvec(x,k),label='discontinuous, k = -2')
k = -3
plt.plot(x,fvec(x,k),label='continuous, k = -3')
#
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
#plt.axis('equal')

#if using termux
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/12/solutions/figs/cont-12-14.pdf')
subprocess.run(shlex.split("termux-open /storage/emulated/0/github/cbse-papers/2020/math/12/solutions/figs/cont-12-14.pdf"))
#else
#plt.show()


