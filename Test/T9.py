

file = open('read.txt', 'r')
data = file.readline()

total = 0
lst = data.split(' ')

for i in range(len(lst)):
    total += int(lst[i])
    
print(total)

file.close()