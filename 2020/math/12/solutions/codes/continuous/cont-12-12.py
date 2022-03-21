#Code by GVV Sharma (works on termux)
#March 19, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the principal value branch for asec(x)


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


asec= np.vectorize(mp.asec)
acos= np.vectorize(mp.acos)
real= np.vectorize(mp.re)

#Input parameters
val = 10
x = np.linspace(-val,val,100)


#Evaluating the expression
f = real(asec(x))

print(acos(-1/2))

plt.plot(x,f,label='$\sec^{-1}(x)$')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
#plt.axis('equal')

#if using termux
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/12/solutions/figs/cont-12-12.pdf')
subprocess.run(shlex.split("termux-open /storage/emulated/0/github/cbse-papers/2020/math/12/solutions/figs/cont-12-12.pdf"))
#else
#plt.show()


