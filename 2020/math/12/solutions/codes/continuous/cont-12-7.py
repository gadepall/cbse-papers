#Code by GVV Sharma (works on termux)
#March 19, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To verify a trigonometric expression


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


#Compatibility with numpy
acos = np.vectorize(mp.acos)
cos = np.vectorize(mp.cos)
asin= np.vectorize(mp.asin)


#Input parameters
c= mp.sqrt(5)
x = 1/c*np.array([1,-2,2,c])


#Evaluating the expression
f = cos(asin(2/c)+acos(x))

print( f)
