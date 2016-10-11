import random

random.seed(0)
N = int(100000 * random.random())
print(N)

y = 0
b = 3
a = -3

for i in range(N):
    x = random.uniform(a, b)
    if -2 <= x <= 2:
       y += (b - a) * (4 - x**2) / N
    else: y += 0

print(y)