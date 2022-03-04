#Code by GVV Sharma (works on termux)
#March 1, 2022
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
r = 3.5
d = 7

e1 = np.array(([1,0]))

#Centre and point 
O = d*e1 #Centre
P = np.array(([0,0]))
theta = mp.asin(r/d)

Q1 = r*mp.cot(theta)*np.array(([mp.cos(theta),mp.sin(theta)]))
Q2 = r*mp.cot(theta)*np.array(([mp.cos(theta),-mp.sin(theta)]))


##Generating all lines
xPQ1 = line_gen(P,Q1)
xPQ2 = line_gen(P,Q2)

##Generating the circle
x_circ= circ_gen(O,r)

#Plotting all lines
plt.plot(xPQ1[0,:],xPQ1[1,:],label='$Tangent1$')
plt.plot(xPQ2[0,:],xPQ2[1,:],label='$Tangent2$')

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circle$')


#Labeling the coordinates
tri_coords = np.vstack((P,Q1,Q2,O)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q1','Q2','O']
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
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-13.pdf')
subprocess.run(shlex.split("termux-open /storage/emulated/0/github/school/ncert-vectors/defs/figs/cbse-10-13.pdf"))
#else
#plt.show()







