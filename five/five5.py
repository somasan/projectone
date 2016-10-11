input = open('twoin.txt', 'r')
output = open('twoout.txt', 'w')
s = input.readline()

A = list(map(int, s.split()))
k = A[0]
N = A[1]

d = [1]*(N-k)
t = k
for i in range(N + 1 - k):
    d.append(t)
    for j in range(k - 1):
        t += d[len(d) - 2 - j]

output.write(str(d[N]))
input.close()
output.close()