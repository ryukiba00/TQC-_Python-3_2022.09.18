
number = int(input())
print('The first ',number,' prime numbers are:')

i = 1
count = 0
while count < number:
    i += 1
    j = 2
    while j <= i:
        if j == i:
            print(i,end = ' ')
            count += 1
            break
        elif i % j == 0:
            break
        else:
            j += 1