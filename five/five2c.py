A = list(map(int, input().split()))
for i in range(0, len(A)):
   if A.count(A[i]) == 1:
       print(A[i], end=' ')