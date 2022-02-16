#Code By GVV Sharma
#Feb 5, 2022
#To find the second number given the first number,
#their LCM and HCF

import numpy as np

#input

num1 =  26
num_lcm = 182
num_hcf = 13


#output
num2 = num_lcm*num_hcf//num1 

#verification
num_lcm_alg = np.lcm(num1,num2)
num_hcf_alg = np.gcd(num1,num2)

print(num1, num2, num_hcf_alg, num_lcm_alg  )
