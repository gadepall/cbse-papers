import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
f = lambda x: x*mp.tan(x)*mp.sin(x)/(mp.sec(x))
val = mp.quad(f, [0, mp.pi])
if (val == mp.pi**2/4):
  print(1)
else:
  print(0)
