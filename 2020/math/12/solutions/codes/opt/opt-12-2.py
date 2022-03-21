#Code by GVV Sharma (works on termux)
#March 19, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Solving a linear program using cvx


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



A = np.array(( [1.0, 2.0], [3.0, 1.0 ])).T
b = np.array([ 28.0, 24.0 ]).reshape((2,-1))
c = np.array([ 30.0, 20.0 ])

x = cp.Variable((2,1),nonneg=True)
#Cost function
f = c@x
obj = cp.Maximize(f)
#Constraints
constraints = [A.T@x <= b]

#solution
cp.Problem(obj, constraints).solve()

print(f.value,x.value)

