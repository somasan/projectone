import numpy as np
import matplotlib.pyplot as plt


a = []
with open('out.txt', 'r') as img:
    for line in img:
        v = list(map(float, line.strip().split(" ")))
        a.append(v)
a = np.array(a)
data = a
values = data.flatten()

b = []
with open('out1.txt', 'r') as img:
    for line in img:
        t = list(map(float, line.strip().split(" ")))
        b.append(t)
b = np.array(b)
data1 = b
values1 = data1.flatten()


plt.subplot(221)
vector = data.flatten()
new_data = vector.reshape(200, 267)
plt.imshow(new_data, cmap=plt.get_cmap('gray'))
plt.colorbar()

plt.subplot(222)
plt.hist(values)

plt.subplot(223)
vector1 = data1.flatten()
new_data1 = vector1.reshape(200, 267)
plt.imshow(new_data1, cmap=plt.get_cmap('gray'))
plt.colorbar()

plt.subplot(224)
plt.hist(values1)


plt.show()