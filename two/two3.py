import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-50, 50.01, 0.01)
y = (np.log(x**2 + 1))/(np.log(1 + np.tan(1/(1 + np.sin(x)**2)))) - (np.abs(x)/10)/(np.log(1 + np.tan(1/(1 + np.sin(x)**2))))
plt.plot(x, y)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.axis('equal')
plt.grid(True)
plt.show()