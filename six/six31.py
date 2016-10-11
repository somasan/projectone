import numpy as np
values = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]

def get_percentile(values, N):
     k =[0.0]
     for i in range(1, N):
         s = np.percentile(values, round(i*100/N))
         k.append(s)
     return k
print(get_percentile(values, 5))
