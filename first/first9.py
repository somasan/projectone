n = input()
s = ''
for i in range(len(n)):
    s = s + n[i] + '*'
print(s[:len(s) - 1])
