input = open('threein.txt', 'r')
output = open('threeout.txt', 'w')
s = input.readline()
a = input.readline()
A = list(map(int, a.split()))
M = 0
N = 0
for i in range(int(s)):
    for j in range(int(s)):
       if A[i] < A[j] and i != j: M += 1
       elif A[i] > A[j] and i != j: N += 1
    if M == N: break
    else:
        M = 0
        N = 0

output.write(str(A[i]))
input.close()
output.close()