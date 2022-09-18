
n = int(input())

total = 0
for i in range(3,n+2, 2):
    total += (i-2)/i

print('%.5f'%(total))