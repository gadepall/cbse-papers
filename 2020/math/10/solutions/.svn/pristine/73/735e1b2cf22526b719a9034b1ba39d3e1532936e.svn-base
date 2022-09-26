# #Code by GVV Sharma
# #December 7, 2019
# #released under GNU GPL
# #Drawing a triangle given 3 sides

# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# image = mpimg.imread('exit-ramp.jpg')
# plt.imshow(image)
# plt.show()

import sys                                          #for path to external scripts
#sys.path.insert(0, '/home/user/txhome/storage/shared/gitlab/res2021/july/conics/codes/CoordGeo')        #path to my scripts
sys.path.insert(0, '/data/data/com.termux/files/home/storage/shared/github/training/math/codes/CoordGeo')        #path to my scripts
#sys.path += ['/data/data/com.termux/files/home/storage/shared/github/training/math/codes/CoordGeo','/data/data/com.termux/files/home/arch/home/user/miniforge3/envs/my-env']

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#local imports
from line.funcs import *

from triangle.funcs import *
from conics.funcs import circ_gen


#sys.path.insert(0, '/home/user/txhome/storage/shared/gitlab/res2021/july/conics/codes/CoordGeo')        #path to my scripts

#if using termux
import subprocess
import shlex
#end if

#Triangle sides
a = 6
b = 5
c = 4


#Triangle coordinates
[A,B,C] = tri_vert(a,b,c)

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Generating the circumcircle
[O,R] = ccircle(A,B,C)
x_circ= circ_gen(O,R)

#Generating the incircle
[I,r] = icircle(A,B,C)
x_icirc= circ_gen(I,r)

#Plotting all lines
# plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
# plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
# plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')


#Plotting the circumcircle
plt.plot(x_circ[0,:],x_circ[1,:],label='$circumcircle$')

#Plotting the circumcircle
plt.plot(x_icirc[0,:],x_icirc[1,:],label='$incircle$')

#Labeling the coordinates
tri_coords = np.vstack((A,B,C,O,I)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','O','I']
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
#plt.savefig('tri_sss.pdf')
plt.savefig('/data/data/com.termux/files/home/storage/shared/gitlab/res2021/july/conics/figs/tri_sss.png')
#subprocess.run(shlex.split("termux-open ./figs/tri_sss.pdf"))
#else
# image = mpimg.imread('tri_sss.png')
# plt.imshow(image)
#plt.show()







