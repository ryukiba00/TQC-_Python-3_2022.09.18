x = 123
y = 123456
z = 12
p = 12
q = 123
r = 123456

# using format
print(format(x, '8d'), format(y, '8d'), format(z, '8d'))
print(format(p, '8d'), format(q, '8d'), format(r, '8d'))

print()

# using %
print('%8d %8d %8d'% (x, y, z))
print('%8d %8d %8d'% (p, q, r))