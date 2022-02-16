#Code By GVV Sharma
#Feb 9, 2022
#To verify a triangle trigonometric identity

import numpy as np

#input parameter

k = np.pi/180 #Convert degree to radian

A = k*30
B = k*100
C = np.pi-(A+B)


#output

print(np.cos((B+C)/2),np.sin(A/2))
