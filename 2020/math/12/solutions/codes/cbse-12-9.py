#Code by GVV Sharma (works on termux)
#January 21, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the intersection of a line and a plane


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


#Line parameters
A = np.array(([1,-4,-4]))
m = np.array(([3,7,2]))

#Plane parameters
n = np.array(([0,0,1]))
c = 0

x = A + (c-n@A)/(n@m)*m
print(x)

