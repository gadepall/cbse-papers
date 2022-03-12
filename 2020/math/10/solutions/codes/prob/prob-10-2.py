#Code by GVV Sharma (works on termux)
#March 7, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To draw a less than ogive for the given data


#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from statistics import median

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


#Input parameters
base= np.linspace(0,70,8)
base = base.reshape([1,8])
values = np.array(([5,15,20,25,15,11,9]))
#base= np.array([104,119,127,135,144,152,162, 170,182])
#values = np.array([305,552,540,472,377,304,250,200])
nvalues = np.size(values)

print(base,values)
A = np.block([base],[values])

#find the cumulative sums
cumulative = np.cumsum(values)
cumulative = np.block([0,cumulative])
imed = np.searchsorted(cumulative, cumulative[nvalues]/2, side='right', sorter=None)
med = base[imed-1] + (cumulative[nvalues]/2-cumulative[imed-1])/values[imed-1]*(base[imed]-base[imed-1])

#print(med, imed,base[imed-1], cumulative[nvalues]/2,cumulative[imed-1], values[imed-1])#,med,cumulative[imed-2])

medcoord = np.array([med,cumulative[nvalues]/2])

# plot the ogive
plt.plot(base, cumulative, 'ro-')
#plt.xlim(100,200)
plt.xlabel('Class Interval')
plt.ylabel('Cumulative Frequency')
plt.legend(loc='best')
plt.grid() # minor
#plt.axis('equal')

#Labeling the coordinates
tri_coords = medcoord.T
plt.scatter(tri_coords[0], tri_coords[1])
vert_labels = ['median']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0], tri_coords[1]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


#if using termux
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/prob-10-2.pdf')
subprocess.run(shlex.split("termux-open /storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/prob-10-2.pdf"))

##else
##plt.show()
#
#
#
#
#
#
#
