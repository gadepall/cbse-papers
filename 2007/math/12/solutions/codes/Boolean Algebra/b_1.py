import numpy as np
a =15
b=9
c=10
out = (a&b&(~c))|(a&(~b)&c)|(a&(~b)&(~c))
print(out)