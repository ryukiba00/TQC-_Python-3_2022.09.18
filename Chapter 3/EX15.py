
n = eval(input())

ans = 0
for i in range(n+1, 1, -1):
    ans += 1 / (i-1)

print(ans)