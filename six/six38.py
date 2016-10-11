import numpy as np
import matplotlib.pyplot as plt

a = []
with open('img.txt', 'r') as img:
    for line in img:
        v = list(map(float, line.strip().split(" ")))
        a.append(v)
a = np.array(a)
data = a
values = data.flatten()

plt.hist(values)
plt.show()