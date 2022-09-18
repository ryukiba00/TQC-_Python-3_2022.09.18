
file = open('read.txt','r')
data = file.read()
file.close()

num = data.split(' ')
total = 0
for i in range(0, len(num)):
    total += eval(num[i])
    
print(total)