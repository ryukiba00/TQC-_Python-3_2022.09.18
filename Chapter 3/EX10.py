import math

n = int(input())
ans = 0

for i in range(2, n+1):
    ans += 1.0 / (math.sqrt(i-1)+math.sqrt(i))
    
print('%.4f' % ans)