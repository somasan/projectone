input = open('fivein.txt', 'r')
output1 = open('fiveout1.txt', 'w')
output2 = open('fiveout2.txt', 'w')
n = input.readline()
m = int(n)
while m != 0:
    k = input.readline()
    output1.write(k)
    m -= 1
t = input.readline()
input.close()
output1.close()

output1 = open('fiveout1.txt', 'r')
count = 0
for i in range(int(n)):
    s = output1.readline()
    A = list(map(int, s.split()))
    if A[0] <= int(t) and A[1] >= int(t):
        count += 1
print(count)

output2.write(str(count))
output2.close()