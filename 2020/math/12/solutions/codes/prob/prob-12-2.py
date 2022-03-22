#Code by GVV Sharma (works on termux)
#March 21, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the probability distribution for 
#the number of sixes obtained following the throw 
#of a dice


#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from numpy import random as RN 
from pylab import *


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


#Sample size
N = int(1e6)
#N =100 

#Generating Samples
x = 1+RN.randint(6,size=(2,N))

#Finding the location of 6 in each die trial
result = np.where(x == 6)
result = np.asarray(result)


#Separating the index vectors for first and second die (0 and 1)
n_zeros = np.count_nonzero(result[0]==0)
first = result[:,0:n_zeros]
second= result[:,n_zeros:N-1]

#Finding the common elements for 0 and 1 (two sixes)
both = set(first[1]).intersection(second[1])
#print(first, second, both, len(both))

#Printing number of sixes for first dice
#print(len(first[1]))

#Printing number of sixes for second dice
#print(len(second[1]))

#Printing number of solo sixes 
#print(len(first[1])+len(second[1]))

#Probability of single 6
one6 = (len(first[1])+len(second[1])-2*len(both))/N

#Printing  number of double sixes 
#print(len(both))

#Probability of double 6
two6 = len(both)/N

#Probability of no 6
no6 = 1 - two6 -one6

#Printing the desired probabilities
print(no6,one6,two6)

#Printing theoretical probabilities
p = 1/6
n = 2
print(mp.binomial(n,0)*(1-p)**2,mp.binomial(n,1)*p*(1-p),mp.binomial(n,2)*p**2*(1-p))


#Mean number of 6s
theory_mean = n*p

#Numerical mean
num_mean = (len(first[1])+len(second[1])-len(both))/N

print(theory_mean,num_mean)





#xy= list(zip(result[0], result[1]))
#print(x,result,result[0:n_zeros,:])
#print(result,first,second)
#print(x,xy)


#I =  np.eye(2)
#e1 =  I[:,0]
##Input parameters
#
#
##Circle parameters
#u1 =  np.array(([-4,0])) 
#f1 = 0
#O = -u1
#r = np.sqrt(LA.norm(u1)**2-f1)
#
##Parabola parameters
#a = 4 
#
##Intersection
#x1 =  np.array(([4,4])) 
#x2 =  np.array(([4,-4])) 
#
###Generating the circle
#len = 20
#x_circ=circ_arc(O,r,90,270,len)
#
##Generating the parabola
#xparab = parab_gen(x_circ[1,:],a)
#
#
##Plotting the circle
#plt.plot(x_circ[0,:],x_circ[1,:],label='Circle')
#
##Plotting the parabola
#plt.plot(xparab,x_circ[1,:],label='Parabola')
#
#
##Shading the region between the arc DB and the square formed by O,D,B
#ind = int(len/2)
#fill_betweenx(x_circ[1,0:ind],xparab[0:ind],x_circ[0,0:ind],facecolor='orange')
#
#
#
##Labeling the coordinates
#tri_coords = np.vstack((O,x1,x2)).T
#plt.scatter(tri_coords[0,:], tri_coords[1,:])
#vert_labels = ['O','$x_1$','$x_2$']
#for i, txt in enumerate(vert_labels):
#    plt.annotate(txt, # this is the text
#                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
#                 textcoords="offset points", # how to position the text
#                 xytext=(0,10), # distance from text to points (x,y)
#                 ha='center') # horizontal alignment can be left, right or center
#
#plt.xlabel('$x$')
#plt.ylabel('$y$')
#plt.legend(loc='best')
#plt.grid() # minor
#plt.axis('equal')
#
##if using termux
#plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/12/solutions/figs/matrix-12-15.pdf')
#subprocess.run(shlex.split("termux-open /storage/emulated/0/github/cbse-papers/2020/math/12/solutions/figs/matrix-12-15.pdf"))
##else
##plt.show()
#
#
#
#
#
#
#
