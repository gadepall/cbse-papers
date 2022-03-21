#Code by GVV Sharma (works on termux)
#March 19, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the inverse of the coefficient matrix and use it to solve a system of equations


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

#Standard basis vectors
I = np.eye(2)
e1 = I[0,:]


#Input matrix
A = np.array(([5,-1,4],[2,3,5],[5,-2,6]))
b = np.array([5,2,-1])
Ainv = LA.inv(A)
x = Ainv@b
print(51*Ainv,x,A@x)


