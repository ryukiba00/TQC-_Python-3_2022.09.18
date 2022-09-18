
a = int(input())
b = int(input())
c = int(input())

gcd = 1
x = 2
while x <= a and x <= b and x <= c:
    if a % x == 0 and b % x ==0 and c % x == 0:
        gcd = x
    x += 1

print('gcd(%d, %d, %d) = %d' % (a, b, c, gcd))