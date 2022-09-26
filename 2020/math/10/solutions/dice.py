import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

n = np.array([2,3]).reshape(2,1)
F = np.array([-2,3]).reshape(2,1)
c = -4
e = 4/5

V = np.linalg.norm(n)**2*np.eye(2) -e**2*n@n.T
u = c*e**2*n-np.linalg.norm(n)**2*F
f = (np.linalg.norm(n)*np.linalg.norm(n))**2-c**2*e**2
print(25*V,25*2*u,f*25)

# N = 5
# n = np.arange(N + 1).reshape(N + 1, 1)   
# xx = np.cos(np.pi * n / N)
# T = np.cos(np.arccos(xx) @ n.T)
# print(T)
# N = 5
# n = np.random.rand(5,1)
# F = np.random.rand(5,1)
#print(n@(F.T@F)@n,(n@F)**2)
#print(n.T@(F@F.T)@n, (n.T@F)**2)
#print(n,F.T)
# n = np.array([1,-4])
# F = np.array([2,3]).reshape(2,1)
#F = np.array([2,4]).reshape(2,1)
#print(n@(F@F.T)@n,(n@F)**2)
#nT= np.reshape(n, (2,-1))
#print(n@x.T)

#Sample size
# simlen = 10000
# #Possible outcomes
# n = range(2,13)
# # Generate X1 and X2
# y = np.random.randint(1,7, size=(2, simlen))

# #Generate X
# X = np.sum(y, axis = 0) 
# #Find the frequency of each outcome
# unique, counts = np.unique(X, return_counts=True)
# #Simulated probability
# psim = counts/simlen
# #Theoretical probability
# n1 = range(2,8)
# n2 = range(8,13)
# panal1 = (n1 -np.ones((1,6)))
# panal2 = (13*np.ones((1,5))-n2)
# panal = np.concatenate((panal1,panal2),axis=None)/36

# #Plotting
# plt.stem(n,psim, markerfmt='o', use_line_collection=True, label='Simulation')
# plt.stem(n,panal, markerfmt='o',use_line_collection=True, label='Analysis')
# plt.xlabel('$n$')
# plt.ylabel('$p_{X}(n)$')
# plt.legend()
# plt.grid()# minor

# #If using termux
# # plt.savefig('figs/pmf.pdf')
# # plt.savefig('figs/pmf.eps')
# # subprocess.run(shlex.split("termux-open figs/pmf.pdf"))
# #else
# #plt.show()

# plt.savefig('/home/user/txhome/storage/shared/gitlab/res2021/july/conics/codes/pmf.png')
# #print(2*3)