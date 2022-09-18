
list1 = []

sum1 = 0
for i in range(0, 12):
    x = int(input())
    list1.append(x)
    if i % 2 == 0:
        sum1 += x
        
count = 0
for i in range(0, 12):
    if count == 3:
        count = 1
        print()
    else:
        count += 1
    print('%3d' % list1[i], end ='')

print()    
print(sum1)