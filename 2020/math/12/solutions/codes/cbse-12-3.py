
#Code by GVV Sharma (works on termux)
#January 20, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the angle between two vectors


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
m_1 = np.array(([1,-1,0]))
m_2 = np.array(([0,1,-1]))

cos_ang = m_1@m_2/(LA.norm(m_1)*LA.norm(m_1))
print(np.arccos(cos_ang),2*np.pi/3)

