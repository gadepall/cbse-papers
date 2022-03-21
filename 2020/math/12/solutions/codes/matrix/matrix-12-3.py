#Code by GVV Sharma (works on termux)
#March 17, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the angle betwwen unit vectors so that a linear combination
#of the vectors is also a unit vector


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

#Standard basis vectors
I = np.eye(2)
e1 = I[0,:]


#Input vectors
b = e1
theta = np.pi/6
a = rot(theta)@b
O = np.zeros((1,2))

#Output vector
c = np.sqrt(3)*a - b
r = 1

#Generating the unit circle

xcirc = circ_gen(O,r)

print(b,a,LA.norm(a),O)


##Input parameters
#r = 3.5
#ap = 12
#theta = mp.atan(r/ap)
#d = r*mp.csc(theta)
#k = 0.7
#bp = (1-k)*ap
#
#
#e1 = np.array(([1,0]))
#
##Centre and point 
#O = d*e1 #Centre
#A = np.array(([0,0]) = np.array(P.tolist(), dtype=float)
#Q = np.array(Q.tolist(), dtype=float)
#O = np.array(O.tolist(), dtype=float)
#B = k*P
#
#
##Reflection
#m = B-O
#n = omat@m
#c = n@O
#
#D = reflect(n,c,P)
#
#
##Finding C
##parameters for line BD
#m1 = B-D
#n1 = omat@m1
#
##parameters for line AQ
#m2 = A-Q
#n2 = omat@m2
##print(n1,n2)
#
##Intersection of BD and AQ
#C = line_intersect(n1,B,n2,A)
#
#
##Perimeter of the triangle ABC
#print(LA.norm(A-B)+LA.norm(B-C)+LA.norm(C-A),ap)
#
###Generating all lines
#xPQ1 = line_gen(A,P)
#xPQ2 = line_gen(A,Q)
#xBC = line_gen(B,C)
#
##Plotting all lines
#plt.plot(xPQ1[0,:],xPQ1[1,:],label='$Tangent1$')
#plt.plot(xPQ2[0,:],xPQ2[1,:],label='$Tangent2$')
#plt.plot(xBC[0,:],xBC[1,:],label='$Tangent3$')
#
##Plotting the circle
plt.plot(xcirc[0,:],xcirc[1,:],label='Unit Circle')
#
#
#Labeling the coordinates
tri_coords = np.vstack((a,b,c,O)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['a','b','c','O']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
#
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
#
#if using termux
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/12/solutions/figs/matrix-12-3.pdf')
subprocess.run(shlex.split("termux-open /storage/emulated/0/github/cbse-papers/2020/math/12/solutions/figs/matrix-12-3.pdf"))
#else
#plt.show()







