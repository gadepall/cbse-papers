#Code by GVV Sharma (works on termux)
#March 18, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the equation of a plane given two points on the plane and a perpendicular plane


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


#Input vectors
a = np.array([1,0,-2])
b = np.array([3,-1,0])
n = np.array([2,-1,1])
c = 8

A = np.block([[a],[b],[n]])
u = np.array([1,1,0])
nsol = LA.solve(A,u)
print(nsol)


