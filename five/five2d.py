A = list(map(int, input().split()))
s = 0
for i in range(0, len(A)):
   s = max(s, A.count(A[i]))
print(s)