import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]

plt.subplot(121)
v, p = np.polyfit(x, y, 1, cov=True)
p_f = np.poly1d(v)
print(sum(p[0:1, 1]))
plt.plot(x, p_f(x))
plt.errorbar(x, y, xerr=sum(p[0:1, 0]), yerr=sum(p[0:1, 1]))
plt.errorbar(x, y, xerr=sum(p[0:, 0]), yerr=sum(p[0:, 1]))
plt.grid(True)


plt.subplot(122)
v, p = np.polyfit(x, y, 2, cov=True)
p_f = np.poly1d(v)
plt.errorbar(x, y, xerr=sum(p[0:1, 0]), yerr=sum(p[0:1, 1]))
plt.errorbar(x, y, xerr=sum(p[0:, 0]), yerr=sum(p[0:, 1]))
plt.plot(x, p_f(x))
plt.grid(True)


plt.show()