#Code By GVV Sharma
#Feb 6, 2022
#To calculate the sum of the terms in an A.P.

import numpy as np


#input parameters

a0= -5 #first term
d = -3#common difference
an = -230#last term

n = (an-a0)/d + 1 #number of terms

Sn = n*(an+a0)/2 #sum of terms


print(n,Sn)
