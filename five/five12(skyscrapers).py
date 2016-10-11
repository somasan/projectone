input = open('scrippersin.txt', 'r')
output1 = open('scrippersrob.txt', 'w')


c = input.readline()
c = c.rstrip()
while len(c) > 0:
    print(c, file=output1, end=' ')
    c = input.readline()
    c = c.rstrip()
input.close()
output1.close()

output1 = open('scrippersrob.txt', 'r')
a = output1.readline()
output1.close()
A = list(map(int, a.split()))


m = max(A)

a = 0
b = 1
count = 0
counter = 0
s = 0
for i in range(len(A) - 1):
    for k in range(len(A) - s):
        for j in range(a, b):
            m = min(m, A[j])
            count += 1
        count *= m

        a += 1
        b += 1
        if count > counter:
            height = m
        counter = max(counter, count)
        count = 0
        m = max(A)
    a = 0
    b = i + 2
    s += 1

with open('scrippersout.txt', 'w') as f:
    print(counter, file=f)
    print(height, file=f)