import numpy as np
import random
values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

def get_percentile(values, N):
     k =[0.0]
     for i in range(1, N):
         s = np.percentile(values, round(i*100/N))
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
def values_equalization(values, add_random = True):
    percentiles = get_percentile(values, 4)
    print(percentiles)
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
    print(new)

values_equalization(values, add_random=True)
