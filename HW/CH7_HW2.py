import random

lst = []
for i in range(10):
    lst.append(random.randint(1, 100))

set1 = set(lst)

print(lst)
print(set1)