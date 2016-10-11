input = open('sevenin.txt', 'r')
s = int(input.readline())
input.close()
if s == 0:
   with open('sevenout.txt', 'w') as f:
       print(1, file=f)
if s == 1:
    with open('sevenout.txt', 'w') as f:
       print(1, file=f)
       print(1, 1, file=f)

if s > 1:
    with open('sevenout.txt', 'w') as f:
       print(1, file=f)
       print(1, 1, file=f)
    for i in range(s - 1):

       prob = open('sevrob.txt', 'r')
       A = prob.readline()
       prob.close()

       L = list(map(int, A.split()))
       a = 0
       b = 1
       count = 0
       c =[1]

       for k in range(len(L) - 1):
           for j in range(a, b + 1):
               count += L[j]
           c.append(count)
           a += 1
           b += 1
           count = 0
       c.append(1)
       with open('sevrob.txt', 'w') as f:
           print(' '.join(map(str, c)), file=f)
       with open('sevenout.txt', 'a') as f:
           print(' '.join(map(str, c)), file=f)
    with open('sevrob.txt', 'w') as f:
        print(1, 1, file=f)
