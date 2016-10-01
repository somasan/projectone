import sys

def fac(n, depth):
    if n == 0:
        print(depth)
        return 1
    else:
        return n*fac(n-1, depth + 1)
print(sys.getrecursionlimit())
print(fac(996, 1))