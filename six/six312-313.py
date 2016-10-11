import numpy as np
import random
import matplotlib.pyplot as plt


a = []
with open('out.txt', 'r') as img:
    for line in img:
        v = list(map(float, line.strip().split(" ")))
        a.append(v)

plt.subplot(121)
b = []
for i in range(100):
    b.append(random.choice(a))
data1 = np.array(b)
plt.imshow(data1, cmap=plt.get_cmap('gray'))
plt.colorbar()

plt.subplot(122)
d =[]
c = random.sample(range(200),100)
for i in range(len(c)):
    d.append(a[c[i]])
data2 = np.array(d)
plt.imshow(data2, cmap=plt.get_cmap('gray'))
plt.colorbar()

plt.show()

