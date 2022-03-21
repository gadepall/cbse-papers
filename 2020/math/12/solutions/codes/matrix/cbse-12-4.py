#Code by GVV Sharma (works on termux)
#January 21, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the coefficient(s) of the characteristic polynomial using the Cayley-Hamilton theorem


#Python libraries for math and graphics
import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0, '/storage/emulated/0/github/school/ncert-vectors/defs/codes/CoordGeo')        #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if


#Input Matrix

A = smp.Matrix(([-3,2],[1,-1]))
lamda = smp.symbols('lamda')
p = A.charpoly(lamda)


print(p)

