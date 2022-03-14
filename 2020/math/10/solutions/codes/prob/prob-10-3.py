#Code by GVV Sharma (works on termux)
# March 13, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To draw a less than ogive for the given data


#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from statistics import median
import pandas as pd
from scipy.ndimage import shift

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


I = np.eye(2)
e2 = I[0:,1]


#Input parameters from excel file
df= pd.read_excel('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/tables/prob-10-3.xlsx')
print(df)
dst = df.to_numpy()[:,1:]


#Data cleaning for finding the mean
temp = dst[0].astype(float)
temp1 = shift(temp, 1, cval=np.NAN)
temp2 = (temp+temp1)/2

#Class mark
clmark = temp2[1:]

#Frequency
nbowl= dst[1].astype(float)[1:]

#Mean
mean = clmark@nbowl/np.sum(nbowl)


print(clmark,nbowl)
print(mean)

nvalues = np.size(dst[0])-1

#Creating numpy matrix of the Age and cumulative frequency of number of people
A = np.block([[dst[0]],[np.cumsum(dst[1])]])

#Locating the lower index for the median class
imed = np.searchsorted(A[1], A[1][nvalues]/2, side='right', sorter=None)-1

#Computing the median point
M = A[:,imed]+ (A[1,nvalues]/2-e2@A[:,imed])/(e2@(A[:,imed+1]-A[:,imed]))*(A[:,imed+1]-A[:,imed])
print(M[0],A)


#Ogive Curve 
plt.plot(A[0,:], A[1,:], 'ro-')
plt.xlabel('Class Interval')
plt.ylabel('Cumulative Frequency')
plt.legend(loc='best')
plt.grid() # minor
#plt.axis('equal')

#Labeling the coordinates
tri_coords = M.T
plt.scatter(tri_coords[0], tri_coords[1])
vert_labels = ['M']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0], tri_coords[1]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


#if using termux
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/prob-10-3.pdf')
subprocess.run(shlex.split("termux-open /storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/prob-10-3.pdf"))

#else
#plt.show()







