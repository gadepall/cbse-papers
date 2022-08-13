
#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from numpy import random as RN 
from pylab import *

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
p = 1/4
n = 16
#print(mp.binomial(n,0)*(1-p)**2,mp.binomial(n,1)*p*(1-p),mp.binomial(n,2)*p**2*(1-p))


#Mean number of 6s
theory_mean = n*p

#Numerical mean
num_mean = (len(first[1])+len(second[1])-len(both))/N

print(theory_mean,num_mean)