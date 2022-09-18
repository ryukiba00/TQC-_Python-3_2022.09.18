
def compute(a, b):
    gcd = 1
    i = 1
    
    while True:
        if i == a or i == b:
            break
        elif a % i == 0 and b % i == 0:
            gcd = i
        i += 1
    
    return gcd

x, y = eval(input())
m, n = eval(input())

p = (x * n + m * y)
q = y * n
g = compute(p, q)

print("%d/%d + %d/%d = %d/%d" % (x, y, m, n,(p/g), (q/g)))