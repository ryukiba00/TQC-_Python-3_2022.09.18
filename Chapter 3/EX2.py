
a = int(input())
b = int(input())
ans = 0

while a <= b:
    if a % 2 == 0:
        ans += a
    a += 1

print(ans)