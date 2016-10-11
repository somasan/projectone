import numpy as np
import random

def get_percentile(values, N):
    k = [0.0]
    for i in range(1, N):
        s = np.percentile(values, round(i * 100 / N))
        k.append(s)
    return k


def get_percentile_number(N):
    percentiles = get_percentile(values, 4)
    for i in range(len(percentiles)):
        if N >= percentiles[i] and N < percentiles[i + 1]:
            return i
            break
        elif N <= min(percentiles):
            return 0
            break
        elif N >= max(percentiles):
            return len(percentiles) - 1
            break


def values_equalization(values, add_random=True):
    percentiles = get_percentile(values, 10)
    step = 1 / len(percentiles)
    new = []
    for i in range(len(values)):
        idx = get_percentile_number(values[i])
        if add_random == True:
            random_noise = random.random() * step
            new_value = idx * step + random_noise
            new.append(new_value)
        else:
            new_value = idx * step
            new.append(new_value)
    return new

a = []
with open('img.txt', 'r') as img:
    for line in img:
        v = list(map(float, line.strip().split(" ")))
        a.append(v)
a = np.array(a)
data = a
values = data.flatten()



vector = data.flatten()
vector = values_equalization(vector, True)
vector = np.array(vector)
new_data = vector.reshape(200, 267)


with open('out1.txt', 'w') as f:
    for i in range(len(new_data)):
        for j in range(len(new_data[i])):
            print(new_data[i][j], end=' ', file=f)
        print(file=f)

