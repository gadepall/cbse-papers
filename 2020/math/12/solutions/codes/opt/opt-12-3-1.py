#Code by GVV Sharma (works on termux)
#March 19, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Algo from Wikipedia
#Solving a mensuration optimization problem using 
#Gradient Descent

#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *
import cvxpy  as cp


import sys                                          #for path to external scripts
sys.path.insert(0,'/storage/emulated/0/github/cbse-papers/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
#from conics.funcs import circ_gen
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if



def S(r,V):
	return np.pi*r**2 + 2*V/r

V = np.pi*125

#Gradient Descent
cur_x = 2 # The algorithm starts at x=2
gamma = 0.001 # step size multiplier
precision = 0.00000001
previous_step_size = 1 
max_iters = 100000000 # maximum number of iterations
iters = 0 #iteration counter

df = lambda r: 2*np.pi*r - 2*V/(r**2)

while (previous_step_size > precision) & (iters < max_iters):
    prev_x = cur_x
    cur_x -= gamma * df(prev_x)
    previous_step_size = abs(cur_x - prev_x)
    iters+=1
print(S(cur_x,V))
print("The local minimum occurs at", cur_x)

r = np.linspace(4,6,20)
S = S(r,V)

plt.plot(r,S)
plt.xlabel('$r$')
plt.ylabel('$S(r)$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/12/solutions/figs/opt-12-3.pdf')
subprocess.run(shlex.split("termux-open /storage/emulated/0/github/cbse-papers/2020/math/12/solutions/figs/opt-12-3.pdf"))
#else
#plt.show()


