#Code By GVV Sharma
#Feb 9, 2022
#To find the  term to be added to the given polynomial
#to make it divisible by another polynomial

import numpy as np
import sympy as smp
from sympy import poly,roots
from sympy.abc import x

#input parameter

px = 2*x**3- 3*x**2+6*x+7
dx = x**2 -4*x + 8
rx = 33-10*x
#output
qx,r1x = smp.div((px+rx),dx)

print(qx,",",r1x)
