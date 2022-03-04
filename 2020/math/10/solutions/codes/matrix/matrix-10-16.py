#Code by GVV Sharma (works on termux)
#March 4, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the intersection of a line with a circle


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
#from conics.funcs import circ_gen
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if


I =  np.eye(2)
e1 =  I[:,0]
#Input parameters

#line parameters
n =  np.array(([1,-1])) #normal vector
m =  omat@n #direction vector
c = 8
q = c/(n@e1)*e1 #x-intercept
print(q)

#circle parameters
V = I
u = np.zeros(2)
r = np.sqrt(544)
f = -r**2
O = -u #Centre

#Points of intersection
#of line with circle
x1,x2 = inter_pt(m,q,V,u,f)
print(x1,x2)

##Generating the line 
k1 = -20
k2 = 20
xline = line_dir_pt(m,q,k1,k2)

##Generating the circle
x_circ= circ_gen(O,r)

#Plotting all lines
plt.plot(xline[0,:],xline[1,:],label='$Chord$')

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circle$')


#Labeling the coordinates
tri_coords = np.vstack((O,x1,x2)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['O','$x_1$','$x_2$']
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
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-16.pdf')
subprocess.run(shlex.split("termux-open /storage/emulated/0/github/school/ncert-vectors/defs/figs/cbse-10-16.pdf"))
#else
#plt.show()







