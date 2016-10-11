import numpy as np
import matplotlib.pyplot as plt


a = []
with open('out.txt', 'r') as img:
    for line in img:
        v = list(map(float, line.strip().split(" ")))
        a.append(v)
new_data = np.array(a)
quantity = 0
value = 0
for i in range(len(new_data)):
    for j in range(len(new_data[i])):
        value += new_data[i][j]
        quantity += 1
print('average value =', value/quantity)