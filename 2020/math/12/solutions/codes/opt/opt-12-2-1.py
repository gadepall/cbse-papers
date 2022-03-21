#Code by GVV Sharma (works on termux)
#March 19, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Solving a linear program using a graphical approach


#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *
import cvxpy  as cp


import sys                                          #for path to external scripts
sys.path.insert(0,'/storage/emulated/0/github/cbse-papers/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
#from conics.funcs import circ_gen
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if


#Constraint lines
n1 = np.array([1,2])
c1 = 28
n2 = np.array([3,1])
c2 = 24
n3 = np.array([1,0])
c3 = 0
n4 = np.array([0,1])
c4 = 0

P1 =LA.solve(np.block([[n1],[n2]]),np.array([c1,c2])) 
P5 =LA.solve(np.block([[n2],[n3]]),np.array([c2,c3])) 
P3 =LA.solve(np.block([[n3],[n4]]),np.array([c3,c4])) 
P6 =LA.solve(np.block([[n4],[n1]]),np.array([c4,c1])) 
P2 =LA.solve(np.block([[n1],[n3]]),np.array([c1,c3])) 
P4 =LA.solve(np.block([[n2],[n4]]),np.array([c2,c4])) 
#print(P1,P2,P3,P4,P5,P6)

#Input parameters

C = np.block([[P1],[P2],[P3],[P4]]).T
print(C)
n = np.array([30,20])


#Profit vector
Pvec = n@C

#Max Profit
Pmax = np.amax(Pvec)

#Locating the index for the max profit
imax = np.where(Pvec==Pmax)
imax= imax[0]

#Optimum point

print(Pvec,imax,C[:,imax])

#Lagrange method

Lmat = np.array([[0,0,1,3],[0,0,2,1],[1,2,0,0],[3,1,0,0]]) 
bvec = np.array([-30,-20,28,24])

print(LA.solve(Lmat,bvec))



#Generating the lines
x12 = line_gen(P1,P2)
x23 = line_gen(P2,P3)
x34 = line_gen(P3,P4)
x41 = line_gen(P4,P1)

#Plotting the lines
plt.plot(x12[0,:],x12[1,:])#,label='Circle')
plt.plot(x23[0,:],x23[1,:])#,label='Circle')
plt.plot(x34[0,:],x34[1,:])#,label='Circle')
plt.plot(x41[0,:],x41[1,:])#,label='Circle')

fill_between(x12[0,:],x12[1,:],color='orange',label='Feasible Region')
fill_between(x41[0,:],x41[1,:],color='orange')#,label='Circle')

#Labeling the coordinates
tri_coords = np.vstack((P1,P2,P3,P4,P5,P6)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P1','$P_2$','$P_3$','$P_4$','$P_5$','$P_6$']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/12/solutions/figs/opt-12-2.pdf')
subprocess.run(shlex.split("termux-open /storage/emulated/0/github/cbse-papers/2020/math/12/solutions/figs/opt-12-2.pdf"))
#else
#plt.show()






