import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *
import cvxpy  as cp



def S(r,V):
	return 2*V/r

V = np.pi*125

#Gradient Descent
cur_x = 2 # The algorithm starts at x=2
gamma = 0.001 # step size multiplier
precision = 0.00000001
previous_step_size = 1 
max_iters = 100000000 # maximum number of iterations
iters = 0 #iteration counter

df = lambda r: -2*V/(r**2)

while (previous_step_size > precision) & (iters < max_iters):
    prev_x = cur_x
    cur_x -= gamma * df(prev_x)
    previous_step_size = abs(cur_x - prev_x)
    iters+=1
print(S(cur_x,V))
print("The local minimum occurs at", cur_x)

r = np.linspace(4,6,20)
S = S(r,V)

plt.plot(r,S)
plt.xlabel('$r$')
plt.ylabel('$S(r)$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()