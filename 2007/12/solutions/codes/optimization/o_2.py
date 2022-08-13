import numpy as np
import cvxpy as cp 
import math
#Declaring Variables
h = cp.Variable(pos=True, name="h")
r = cp.Variable(pos=True, name="r")
#Computing surface area
S = 2*np.pi*r*h

constraints = [
        np.pi*r**2*h == 125, h== math.sqrt(2)*r
]

#Problem Formulation
problem = cp.Problem(cp.Minimize(S), constraints)

#Checking cuvature of the objective function
print(S.log_log_curvature)

#Checking if the problem is DGP
print("Is this problem DGP?", problem.is_dgp())


#solution
problem.solve(gp=True)
print(problem.value, h.value, r.value)