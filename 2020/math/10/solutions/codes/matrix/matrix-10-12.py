#Code by GVV Sharma (works on termux)
#March 1, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To draw two similar triangles


#Python libraries for math and graphics
import numpy as np
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
#ABC
c = 5 
a = 6
k = 3/4
theta = np.pi/3
A = c*np.array(([np.cos(theta),np.sin(theta)]))
B = np.array(([0,0]))
e1 = np.array(([1,0]))
C = a*e1

#PQR
theta = np.pi/3
P = k*c*np.array(([np.cos(theta),np.sin(theta)]))
Q = np.array(([0,0]))
e1 = np.array(([1,0]))
R = k*a*e1



##Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(C,B)
x_CA = line_gen(A,C)

x_PQ = line_gen(P,Q)
x_QR = line_gen(Q,R)
x_RP = line_gen(R,P)


#Define subplots
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2, sharex=ax1, sharey=ax1)


#Subplot 1

#Plotting all lines
ax1.plot(x_AB[0,:],x_AB[1,:])#,label='$Diameter$')
ax1.plot(x_BC[0,:],x_BC[1,:])#,label='$Diameter$')
ax1.plot(x_CA[0,:],x_CA[1,:])#,label='$Diameter$')
#ax1.plot(x_PQ[0,:],x_PQ[1,:])#,label='$Diameter$')


#Labeling the coordinates
tri_coords = np.vstack((A,B,C)).T
ax1.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C']
for i, txt in enumerate(vert_labels):
    ax1.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

#ax1.xlabel('$x$')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
#ax1.legend(loc='best')
ax1.grid() # minor
#ax1.axis('equal')


#Subplot 2

#Plotting all lines
ax2.plot(x_PQ[0,:],x_PQ[1,:])#,label='$Diameter$')
ax2.plot(x_QR[0,:],x_QR[1,:])#,label='$Diameter$')
ax2.plot(x_RP[0,:],x_RP[1,:])#,label='$Diameter$')


#Labeling the coordinates
tri_coords = np.vstack((P,Q,R)).T
ax2.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q','R']
for i, txt in enumerate(vert_labels):
    ax2.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
#ax2.legend(loc='best')
ax2.grid() # minor
#ax2.axis('equal')

#if using termux
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-12.pdf')
subprocess.run(shlex.split("termux-open /storage/emulated/0/github/school/ncert-vectors/defs/figs/cbse-10-12.pdf"))
#else
#plt.show()







