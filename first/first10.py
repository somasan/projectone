n = input()
a = n.replace('h', 'H')
s = a.replace('H', 'h', 1)
d = s[::-1]
a = d.replace('H', 'h', 1)
k = a[::-1]
print(k)
