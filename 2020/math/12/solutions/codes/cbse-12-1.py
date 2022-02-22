

#Code by GVV Sharma (works on termux)
#January 18, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the area of a triangle using the cross product.


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
A = np.array(([1,2,3]))
B = np.array(([-3,-2,1]))

C = np.cross(A,B)
print(C,0.5*LA.norm(C),3*np.sqrt(5))
