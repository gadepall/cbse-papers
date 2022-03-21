#Code by GVV Sharma (works on termux)
#March 19, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To verify a tan identity in trigonometry


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

#Input parameters
expr1 = mp.atan(1/4) + mp.atan(2/9)
expr2 = 1/2*mp.asin(4/5) 
eps = 1e-8



if (mp.fabs(expr1-expr2) <= eps):
    print("Identity is correct")
else:
    print("Identity is incorrect")
