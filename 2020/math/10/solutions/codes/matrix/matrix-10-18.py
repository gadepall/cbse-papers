#Code by GVV Sharma (works on termux)
#March 6, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To construct a circle and two tangents to it from a point outside


#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0,'/storage/emulated/0/github/cbse-papers/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

#Input parameters
r = 4
alpha = 90 *np.pi/180
theta = alpha/2
l = r*mp.cot(theta)
print(l)

d = r*mp.csc(theta)

e1 = np.array(([1,0]))

#Centre and point 
O = d*e1 #Centre
P = np.array(([0,0]))

Q = l*np.array(([mp.cos(theta),-mp.sin(theta)]))
R = l*np.array(([mp.cos(theta),mp.sin(theta)]))
R = np.array(R.tolist(), dtype=float)
Q = np.array(Q.tolist(), dtype=float)
O = np.array(O.tolist(), dtype=float)


##Generating all lines
xPQ = line_gen(P,Q)
xPR = line_gen(P,R)
xOP= line_gen(O,P)
xOQ = line_gen(O,Q)

##Generating the circle
x_circ= circ_gen(O,r)

#Plotting all lines
plt.plot(xPQ[0,:],xPQ[1,:],label='$Tangent1$')
plt.plot(xPR[0,:],xPR[1,:],label='$Tangent2$')
plt.plot(xOQ[0,:],xOQ[1,:],label='$Radius$')
plt.plot(xOP[0,:],xOP[1,:],'-.',label='$Radius$')

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circle$')


#Labeling the coordinates
tri_coords = np.vstack((P,Q,R,O)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q','R','O']
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
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-18.pdf')
subprocess.run(shlex.split("termux-open /storage/emulated/0/github/school/ncert-vectors/defs/figs/cbse-10-18.pdf"))
#else
#plt.show()







