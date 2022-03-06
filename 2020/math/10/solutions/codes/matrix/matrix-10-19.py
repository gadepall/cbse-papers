#Code by GVV Sharma (works on termux)
#March 6, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To draw similar triangles using BPT


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
k = 1.5
ae = 2.7
ec = ae/k
print(ec)
b = ae*(1+1/k)
theta = np.pi/3
B = b*np.array(([np.cos(theta),-np.sin(theta)]))
A = np.array(([0,0]))
e1 = np.array(([1,0]))
C = b*e1
E = (k*C+A)/(k+1)
D = (k*B+A)/(k+1)


##Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(C,B)
x_CA = line_gen(A,C)
x_DE = line_gen(D,E)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:])#,label='$Diameter$')
plt.plot(x_BC[0,:],x_BC[1,:])#,label='$Diameter$')
plt.plot(x_CA[0,:],x_CA[1,:])#,label='$Diameter$')
plt.plot(x_DE[0,:],x_DE[1,:])#,label='$Diameter$')


#Labeling the coordinates
tri_coords = np.vstack((A,B,C,D,E)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','E']
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
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-19.pdf')
subprocess.run(shlex.split("termux-open /storage/emulated/0/github/school/ncert-vectors/defs/figs/cbse-10-19.pdf"))
#else
#plt.show()







