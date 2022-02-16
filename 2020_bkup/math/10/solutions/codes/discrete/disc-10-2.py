#Code By GVV Sharma
#Feb 5, 2022
#To check for divisibility

import numpy as np

#Input value
n = 15

x = 12**n

q = x//10
r = x%10

#Finding the quotient and remainder
[q,r] = divmod(x, 10)

print(q, r)
