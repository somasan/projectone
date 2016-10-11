import numpy as np
values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

def get_percentile(values, N):
     k =[0.0]
     for i in range(1, N):
         s = np.percentile(values, round(i*100/N))
         k.append(s)
     return k

def get_percentile_number(N):
    percentiles = get_percentile(values, 4)
    print(percentiles)
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
def value_equalization(value):
    percentiles = get_percentile(values, 5)
    idx = get_percentile_number(value)
    step = 1 / len(percentiles)
    new_value = idx * step
    print(new_value)

value_equalization(5.5)
