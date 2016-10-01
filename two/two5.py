import matplotlib.pyplot as plt
import numpy as np

s = input()
x = np.arange(-10, 10.01, 0.01)

plt.xkcd()
plt.plot(x, eval(s))

plt.show()