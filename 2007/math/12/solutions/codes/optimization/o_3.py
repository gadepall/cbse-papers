import numpy as np
import cvxpy as cp
c= np.array([1,1])
P= np.array([[2,5],[8,5],[-1,0],[0,-1]])
Q= np.array([100,200,0,0])
def optimum(x):
  return c@x # defining the optimization function
# defining the variable
x= cp.Variable(2)
# assigning constraints
constraints = [P@x<=Q] 
# defining ojective
objective= cp.Minimize(-(c@x))
#defining the problem
prob= cp.Problem(objective,constraints)
# solving the problem
prob.solve()
#printing the optimum value
print("The optimum no. of servings :", x.value)
print("The optimum :", optimum(x.value))