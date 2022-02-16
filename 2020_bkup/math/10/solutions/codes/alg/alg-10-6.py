#Code By GVV Sharma
#Feb 9, 2022
#To find the zeros of the quotient, given the polynomial and the  divisor 

import numpy as np
import sympy as smp
from sympy import poly,roots
from sympy.abc import x

#input parameter

px = 2*x**4-x**3 - 11*x**2+5*x+5
dx = (x+smp.sqrt(5))*(x-smp.sqrt(5))
#output
qx,rx = smp.div(px,dx)

print(qx,",",rx)
print(roots(qx))
