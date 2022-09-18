a, b, c = eval(input('Enter a, b, c: '))
d = b*b - 4*a*c

if d > 0:
    print('Has two different solutions')
elif d == 0:
    print('Has one solution')
else:
    print('No solution')

print('Over')