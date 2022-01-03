
import numpy as np
#(CBSE 2007-Question 21)
A=np.array([7,10])
A.resize(2,1)
B=np.array([-2,5])
B.resize(2,1)
C=np.array([3,-4])
C.resize(2,1)
#checking the right angle
if ((A-C).T@(B-C)==0):
	print("ABC is a right triangle and right angle at c")
elif ((A-B).T@(C-B)==0):
	print("ABC is a right triangle and right angle at B")
elif ((B-A).T@(C-A)==0):
	print("ABC is a right triangle and right angle at A")
else:
	print("ABC is a not right triangle")
if((A-C).T@(B-C)==(A-B).T@(C-B)):
    print("ABC is a isosceles and AC=AB")
elif((B-A).T@(C-A)==(A-B).T@(C-B)):
    print("ABC is a isosceles and BC=AC")
elif((B-A).T@(C-A)==(A-C).T@(B-C)):
    print("ABC is a isosceles and BC=AB")
else:
    print("ABC is a not isosceles triangle")