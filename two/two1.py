import numpy as np
x = int(input())
y = (np.log((np.exp(1/(np.sin(x) + 1)))/(5/4 + 1/(x**15))))/(np.log(1 + x**2))
z = 1/((np.sin(x) + 1) * (np.log(1 + x**2))) - (np.log(5/4 + 1/(x**15)))/(np.log(1 + x**2))
print(y, z)

