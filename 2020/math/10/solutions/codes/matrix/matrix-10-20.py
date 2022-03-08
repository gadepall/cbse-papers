#Code by GVV Sharma (works on termux)
#March 7, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To draw a circle with a tangent and chord subtending an angle at the centre


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

#Circle parameters
r = 5
B = np.zeros(2)
O =  np.array(([0,r])) #normal vector
P =  np.array(([-3,0])) #normal vector
thetadeg = 100
theta = thetadeg*np.pi/180
ab = 2*r*np.sin(theta/2)
A =  ab*np.array(([-np.cos(theta/2),np.sin(theta/2)]))


##Generating the line 
m = e1
k1 = -10
k2 = 10
xline = line_dir_pt(m,B,k1,k2)
xAB = line_gen(A,B)
xOB = line_gen(O,B)
xOA = line_gen(A,O)

##Generating the circle
x_circ= circ_gen(O,r)

#Plotting all lines
plt.plot(xline[0,:],xline[1,:],label='Tangent')
plt.plot(xAB[0,:],xAB[1,:],label='Chord')
plt.plot(xOA[0,:],xOA[1,:],label='Radius')
plt.plot(xOB[0,:],xOB[1,:],label='Radius')

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='Circle')


#Labeling the coordinates
tri_coords = np.vstack((O,A,B,P)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['O','A','B','P']
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
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-20.pdf')
subprocess.run(shlex.split("termux-open /storage/emulated/0/github/school/ncert-vectors/defs/figs/cbse-10-20.pdf"))
#else
#plt.show()







