A = list(map(int, input().split()))
A.insert(0, A.pop())
print(' '.join(map(str, A)))