
n = int(input())

for i in range(1, n+1):
    x = int(input())
    ans = 0
    
    print('Sum of all digits of %d is ' % (x),end = '')
    
    while x != 0:
        ans += (x%10)
        x //= 10
    
    print('%d' % (ans))