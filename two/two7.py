import matplotlib.pyplot as plt
import numpy as np

a = float(input('odd a != 1 \n',))
b = float(input('0 < b < 1 \n',))
x = np.arange(-2, 2.01, 0.01)
y = 0
for n in range(100):
    w = b**n *(np.cos(a**n * np.pi * x))
    y += w
plt.plot(x, y)
plt.grid(True)


plt.show()
