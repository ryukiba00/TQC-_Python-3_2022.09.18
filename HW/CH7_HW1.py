import random

lst = []
for i in range(10):
    lst.append(random.randint(1, 100))

tup = tuple(lst)

print(lst)
print(tup)