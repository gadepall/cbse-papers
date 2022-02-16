#Code By GVV Sharma
#Feb 9, 2022
#To find the remainder, given the polynomial and the  divisor 

import numpy as np
import sympy as smp
from sympy import poly
from sympy.abc import x

#input parameter

px = x**4-3*x**2+5*x-9
dx = x**2+3
#output
qx,rx = smp.div(px,dx)

print(qx,",",rx)
