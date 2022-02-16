#Code By GVV Sharma
#Feb 7, 2022
#To find the speed of the stream given the speed of the boat and
#the additional time taken to travel upstream

import numpy as np

#input parameter

v = 18 #speed of the boat
t = 1 #additional time taken
d = 24 #distance
coeff = [t, 2*d, -t*v**2]

#output

xth = -d + np.sqrt(d**2 + t**2*v**2) #theory
xnum = np.roots(coeff)#numerical
print(xth,xnum)
