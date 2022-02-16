#Code By GVV Sharma
#Feb 9, 2022
#To calculate a trigonometric expression

import numpy as np

#input parameter

A = 2*np.pi/5

cotA = 1/(np.tan(A))

#output
y1 = (1+np.tan(A)**2)/(1+ cotA**2)
y2 = np.tan(A)**2

print(y1,y2)
