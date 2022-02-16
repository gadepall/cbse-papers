
#Code by GVV Sharma (works on termux)
#January 18, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To verify if the given vertices belong to an isosceles triangle


#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts

sys.path.insert(0,'/storage/emulated/0/github/cbse-papers/CoordGeo')
#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

#Input parameters
A = np.array(([7,10]))
B = np.array(([-2,5]))
C = np.array(([3,-4]))

if (C-B)@(C-A) == (A-C)@(A-B):
    print("AB=BC, The triangle is isosceles")

#
#Generating all lines
x_AB = line_gen(A,B)
x_BC= line_gen(B,C)
x_CA = line_gen(C,A)
#
#
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB=BC$')
plt.plot(x_BC[0,:],x_BC[1,:])#,label='$Diameter$')
plt.plot(x_CA[0,:],x_CA[1,:])#,label='$Diameter$')
#
#
#Labeling the coordinates
tri_coords = np.vstack((A,B,C)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C']
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
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-5.pdf')
subprocess.run(shlex.split("termux-open '/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-5.pdf'")) 
#else
#plt.show()
