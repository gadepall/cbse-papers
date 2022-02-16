#Code By GVV Sharma
#Feb 9, 2022
#To calculate a trigonometric expression

import numpy as np

#input parameter

k = np.pi/180

x = k*60
y=k*45
h = 1.6

cotx = 1/np.tan(x)
coty = 1/np.tan(y)

#output
d = h*cotx/(coty-cotx)
print(d,h/(np.sqrt(3)-1))
