A = list(map(int, input().split()))

b = []

if len(A) % 2 == 1:
   for i in range(0, len(A)//2):
      b.append(A.pop(0))
      b.append(A.pop())
   b.append(A.pop())
else:
    for i in range(0, len(A)//2):
        b.append(A.pop(0))
        b.append(A.pop())

print(' '.join(map(str, b)))