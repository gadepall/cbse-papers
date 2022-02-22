#Code by GVV Sharma (works on termux)
#January 23, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find if the given line is contained in the given plane


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


#line direction vector
m = np.array(([3,1,-1]))

#plane normal vector
n = np.array(([1,-5,-2]))

if m@n==0:
    print("The line lies within the plane")

