#Code by GVV Sharma (works on termux)
# March 14 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the mode of the given data


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
df= pd.read_excel('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/tables/prob-10-4.xlsx')
print(df)
dst = df.to_numpy()[:,1:]
nvalues = np.size(dst[0])-1

#Creating numpy matrix of the given data
A = np.block([[dst[0]],[dst[1]]])
A = np.array(A.tolist(), dtype=float)
Amax = np.amax(A[1])

#Locating the index for the mode class
imed = np.where(A[1]==Amax)
imed = imed[0]

P = np.array([A[0,imed],A[1,imed]])
Q = np.array([A[0,imed-1],A[1,imed-1]])
R = np.array([A[0,imed-1],A[1,imed]])
S = np.array([A[0,imed],A[1,imed+1]])

#P = np.array(P.tolist(), dtype=float)
#Q = np.array(Q.tolist(), dtype=float)
#R = np.array(R.tolist(), dtype=float)
#S = np.array(S.tolist(), dtype=float)

#Finding the mode
n1 = omat@(P-Q)
n2 = omat@(R-S)


#Computing the mode
M = line_intersect(n1.T,P,n2.T,R)
Mx = np.array([M[0],0])
print(Mx)


#Generating PQ and RS
xPQ = line_gen(P,Q)
xRS = line_gen(R,S)

#generating the mode line
xM = line_gen(M,Mx)


#Plotting the bar graph for the data
plt.bar(A[0,:],A[1,:],width=10)

#Plotting the lines PQ and RS
plt.plot(xPQ[0,:],xPQ[1,:],color='red')#,label='$Diameter$')
plt.plot(xRS[0,:],xRS[1,:],color='orange')#,label='$Diameter$')

#Plotting the Mode line
plt.plot(xM[0,:],xM[1,:],color='yellow')#,label='$Diameter$')


#Labeling the coordinates
tri_coords = np.block([[P.T],[Q.T],[R.T],[S.T],[M],[Mx]]).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q','R','S','M','Mx']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

#if using termux
plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/prob-10-4.pdf')
subprocess.run(shlex.split("termux-open /storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/prob-10-4.pdf"))
#
##else
##plt.show()







