
#Code by GVV Sharma (works on termux)
#January 19, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the foot of the perpendicular from a point to a line in 3D


#Python libraries for math and graphics
import numpy as np
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

#Input parameters
P = np.array(([2,-3, 4]))
A = np.array(([0,0, 0]))
m = np.array(([0,1, 0]))

x = A + (m@(P-A)/LA.norm(m)**2)*m

print(x)
