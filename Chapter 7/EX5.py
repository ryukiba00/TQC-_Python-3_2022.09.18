

set1 = set()
set2 = set()
set3 = set()

print('Input to set1: ')
for i in range(0,5):
    x = int(input())
    set1.add(x)

print('Input to set2: ')
for i in range(0,3):
    x = int(input())
    set2.add(x)

print('Input to set3: ')
for i in range(0,9):
    x = int(input())
    set3.add(x)

print('set2 is subset of set1: ', set2.issubset(set1))
print('set3 is superset of set1: ', set3.issuperset(set1))