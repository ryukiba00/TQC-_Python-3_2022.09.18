
set1 = set()
print('Input set1 data:')
while True:
    x = int(input())
    if x == -9999:
        break
    else:
        set1.add(x)

set2 = set()
print('Input set2 data:')
while True:
    x = int(input())
    if x == -9999:
        break
    else:
        set2.add(x)

print('set1 ',set1)
print('set2', set2)
print('set1 is a subset of set2: ', set1.issubset(set2))
print('set1 is a superset of set2: ', set1.issuperset(set2))
        
