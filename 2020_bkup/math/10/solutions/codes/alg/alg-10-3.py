#Code By GVV Sharma
#Feb 9, 2022
#To find the speed of the stream given the speed of the boat and
#the additional time taken to travel upstream

import numpy as np

#input parameter

coeff = [1, 3, 2]

#output

xnum = np.roots(coeff)#numerical
sumr = np.sum(xnum)
prodr = np.prod(xnum)

print(xnum,sumr,prodr)
