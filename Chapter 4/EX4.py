
n = int(input())

if n == 0:
    print('0')
else:
    list0 = list(str(n))
    for i in range(len(list0)-1, -1, -1):
        print(list0[i],end = '')
    