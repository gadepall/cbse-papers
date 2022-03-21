#Code by GVV Sharma (works on termux)
#March 19, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To compute an integral


#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *

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

cos= np.vectorize(mp.cos)

#Input parameters
fx = lambda x: x*mp.cos(x)**2

val = mp.quad(fx, [-mp.pi/2, mp.pi/2])
print(val)


#Input parameters
val = np.pi/2
x = np.linspace(-val,val,100)


#Evaluating the expression
f = x*cos(x)**2
f = np.array(f.tolist(), dtype=float)

fill_between(x,f,color='orange',label='Area')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
#plt.axis('equal')

#if using termux
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/12/solutions/figs/cont-12-13.pdf')
subprocess.run(shlex.split("termux-open /storage/emulated/0/github/cbse-papers/2020/math/12/solutions/figs/cont-12-13.pdf"))
#else
#plt.show()





