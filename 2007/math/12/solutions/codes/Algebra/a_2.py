import numpy as np
import mpmath as mp
r=40
g=9.8
u=28
t = 0.5*mp.asin((r*g)/(u**2))
print(mp.degrees(t))
print(mp.degrees((np.pi/2)-t))