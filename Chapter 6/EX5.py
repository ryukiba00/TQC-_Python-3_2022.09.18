
list1 = []
for i in range(10):
    list1.append(eval(input()))
    
sum1 = sum(list1)-max(list1)-min(list1)
print(sum1)
print('%.2f' % (sum1/8))