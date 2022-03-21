#Code by GVV Sharma (works on termux)
#January 21, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the distance between two parallel planes


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
n = np.array(([2,1,-2]))
c1 = 6
c2 = 0

#Distance between the planes
d = np.abs(c1-c2)/LA.norm(n)
print(d)

