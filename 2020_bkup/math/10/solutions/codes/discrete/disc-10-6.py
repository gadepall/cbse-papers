#Code By GVV Sharma
#Feb 6, 2022
#To find the sequences that are in A.P.

import numpy as np

#input sequences
x1 = np.array([-1.2,0.8,2.8])
x2 = np.array([3,3+np.sqrt(2),3+2*np.sqrt(2),3+3*np.sqrt(2)])
x3 = np.array([4/3,7/3,9/3,12/3])
x4 = np.array([-1/5,-2/5,-3/5])

#diff seqences
x1diff = np.diff(x1)
x2diff = np.diff(x2)
x3diff = np.diff(x3)
x4diff = np.diff(x4)


print(x1diff,x2diff,x3diff,x4diff)
