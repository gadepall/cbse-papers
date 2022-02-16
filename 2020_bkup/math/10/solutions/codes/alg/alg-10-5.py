#Code By GVV Sharma
#Feb 9, 2022
#To verify the condition for equal roots in  quadratic equation

import numpy as np

#input parameter

k = 0

a = 2 
b = k 
c = 2 


#output
D = b**2 - 4*a*c #Discriminant

if D==0:
    print("The equation has equal roots")
else:
    print("The equation has unequal roots")


