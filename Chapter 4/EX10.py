
n = int(input())

for i in range(0, n):
    for j in range(1, n-i):
        print(' ', end = '')
    for k in range(0,i*2+1):
        print('*',end = '')
    print()