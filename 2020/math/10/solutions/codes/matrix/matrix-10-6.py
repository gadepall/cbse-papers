#Code by GVV Sharma (works on termux)
#February 13, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the fourth vertex and the diagonal given three vertices of a rectangle


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
A = np.array(([0,-3]))
B = np.array(([4,0]))
O = np.array(([0,0]))

#Length of the diagonal
d = LA.norm(A-B)
print(d)

#Fourth vertex
C = A+B-O

##Generating all lines
x_AB = line_gen(A,B)
x_OB = line_gen(O,B)
x_OA = line_gen(O,A)
x_AC = line_gen(A,C)
x_BC = line_gen(C,B)


#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:])#,label='$Diameter$')
plt.plot(x_OA[0,:],x_OA[1,:])#,label='$Diameter$')
plt.plot(x_OB[0,:],x_OB[1,:])#,label='$Diameter$')
plt.plot(x_AC[0,:],x_AC[1,:])#,label='$Diameter$')
plt.plot(x_BC[0,:],x_BC[1,:])#,label='$Diameter$')


#Labeling the coordinates
tri_coords = np.vstack((A,B,O,C)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','O','C']
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
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-6.pdf')
subprocess.run(shlex.split("termux-open  /storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-6.pdf"))
#else
#plt.show()







