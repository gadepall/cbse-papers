#Code by GVV Sharma (works on termux)
#March 19, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the point at which maximum profit occurs


#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *


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


#Input parameters

C = np.array(([0,0,2,5,6],[0,8,7,4,0]))
n = np.array([3,2])


#Profit vector
Pvec = n@C

#Max Profit
Pmax = np.amax(Pvec)

#Locating the index for the max profit
imax = np.where(Pvec==Pmax)
imax= imax[0]

#Optimum point

print(Pvec,imax,C[:,imax])


