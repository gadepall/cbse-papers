#Code by GVV Sharma (works on termux)
#Feb 11, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the intersection of the line joining the given points
#with the y-axis
#two given points

#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0, '/storage/emulated/0/github/cbse-papers/CoordGeo')        #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if



#Given points
A = np.array(([6,-4]))
B = np.array(([-2,-7]))

#Standard Basis vectors
e_1 = np.array(([1,0]))
e_2 = np.array(([0,1]))

#Ratio 
k =  -((e_1@A)/(e_1@B))

#y-coordinate
y = (k*e_2@B+e_2@A)/(k+1)
P = y*e_2

print(k,P)





##Generating all lines
x_AB = line_gen(A,B)


#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')


#Labeling the coordinates
tri_coords = np.vstack((A,B,P)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','P']
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
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-4.pdf')
subprocess.run(shlex.split("termux-open '/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-4.pdf'")) 
#else
#plt.show()







