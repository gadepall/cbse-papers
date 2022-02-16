#Code By GVV Sharma
#Feb 7, 2022
#To find the polynomial, given the quotient, divisor and remainder

import numpy as np
from sympy import poly
from sympy.abc import x

#input parameter

d = x**2-4
r = 3
q = x

#output
px = poly(d*q+r)

print(px)
