input = open('eightin.txt', 'r')
output = open('eightout.txt', 'w')

s = int(input.readline())
print(str(sum([i**2 for i in range(s) if i % 3 == 1])), file=output)

input.close()
output.close()