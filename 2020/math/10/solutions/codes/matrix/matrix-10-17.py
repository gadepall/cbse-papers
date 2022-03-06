#Code by GVV Sharma (works on termux)
#March 6, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To draw a semi-circle and parallelogram on the same base


#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *

import sys                                          #for path to external scripts
sys.path.insert(0,'/storage/emulated/0/github/cbse-papers/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

#input parameters
ab = 12

#circular arc parameters
O = np.zeros(2) #Centre
r =ab/2 

#parallelogram parameters

A =  np.array(([-r,0])) 
B =  np.array(([r,0])) 
D =  np.array(([0,r])) 
C = B+D-A


#Finding the desired area
#pgm area
A1 = 2*r**2
A2 = np.pi/4*r**2
print(A1-A2,9*(8-np.pi))


#Generating the semi circle
x_circ= circ_arc(O,r,180)


#Generating the paralellogram 
xAB = line_gen(A,B)
xOD = line_gen(O,D)
xBC = line_gen(C,B)
xCD = line_gen(C,D)
xAD = line_gen(A,D)

#Plotting all lines
plt.plot(xAB[0,:],xAB[1,:])#,label='$Chord$')
plt.plot(xBC[0,:],xBC[1,:])#,label='$Chord$')
plt.plot(xCD[0,:],xCD[1,:])#,label='$Chord$')
plt.plot(xOD[0,:],xOD[1,:])#,label='$Chord$')


#Shading regions
#Shading triangle AOD
fill_between(xAD[0,:],xAD[1,:],facecolor='orange')
x1 = np.linspace(O[0],B[0],25)
y1 = 6*np.ones(25)
z1 = np.sqrt(6**2-x1**2)
#Shading the region between the arc DB and the square formed by O,D,B
fill_between(x1,y1,z1,facecolor='orange')
#Shading the region above BC
fill_between(xBC[0,:],xBC[1,:],y1[0:10],facecolor='orange')

#Plotting the semicircle
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circle$')


#Labeling the coordinates
tri_coords = np.vstack((O,A,B,C,D)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['$O$','$A$','$B$','$C$','$D$']
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
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-17.pdf')
subprocess.run(shlex.split("termux-open /storage/emulated/0/github/school/ncert-vectors/defs/figs/cbse-10-17.pdf"))
#else
#plt.show()







