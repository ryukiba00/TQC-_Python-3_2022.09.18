

file = open('scores.dat','r')
data = file.readline()

count = 0
sum1 = 0
while data != '':
    lst = data.split(' ')
    sum1 += eval(lst[1])
    count += 1
    data = file.readline()

print('average score: %.2f' % (sum1/count))

file.close()