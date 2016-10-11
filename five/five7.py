input = open('fourin.txt', 'r')
output = open('fourout.txt', 'w')
a = input.readline()

A = list(map(int, a.split()))
n = 10
for i in range(0,9):
    if A[i] == 2 and A[i+1] == 5:
        A[i] = 0
        n -= 1
s = sum(A)//n

output.write(str(s))
input.close()
output.close()