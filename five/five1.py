A = list(map(int, input().split()))

print(' '.join(map(str, [A[i] for i in range(len(A)) if i % 2 == 0])))
print(max(A), ' '.join(map(str, [i for i in range(len(A)) if A[i] == max(A)])))
print(' '.join(map(str, A[::-1])))