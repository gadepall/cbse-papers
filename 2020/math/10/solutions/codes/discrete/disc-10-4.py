#Code By GVV Sharma
#Feb 5, 2022
#To find the sum of the first 100
#natural numbers

import numpy as np

#input
n = 51

#generate numbers

x = np.linspace(1,n,n)


#Find sum
sumx = np.sum(x) #simulation
sumxt = n*(n+1)/2 #theory



print(n,sumx,sumxt)
