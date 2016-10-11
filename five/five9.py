input = open('sixin.txt', 'r')
output = open('sixout.txt', 'w')
s = int(input.readline())
a = input.readline()
A = list(map(int, a.split()))
t = int(input.readline())
a = 0
b = t
count = 0
counter = 0
for i in range(s - t + 1):
    for j in range(a, b):
        count += A[j]
    a += 1
    b += 1
    counter = max(counter, count)
    count = 0
print(counter)



output.write(str(counter))
input.close()
output.close()