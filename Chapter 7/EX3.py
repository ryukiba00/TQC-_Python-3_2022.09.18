
tuple1 = ()
while True:
    x = input()
    if x == 'end':
        break
    else:
        tuple1 += (x,)

print(tuple1)
print(tuple1[0:2])
print(tuple1[-3:])