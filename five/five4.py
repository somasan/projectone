input = open('firstin.txt', 'r')
output = open('firstout.txt', 'w')
s = input.readline()
a = input.readline()
A = list(map(int, s.split()))

for i in range(int(a)):
     t = A.pop()
     A.insert(t % len(A), t)

output.write(' '.join(map(str, A)))
input.close()
output.close()