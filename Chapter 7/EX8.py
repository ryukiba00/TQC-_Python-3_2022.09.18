
dict1 = {}
print('Create dict1: ')
while True:
    x = input('Key: ')
    if x == 'end':
        break
    y = input('Value: ')
    if y == 'end':
        break
    
    dict1[x] = y
    
dict2 = {}
print('Create dict2: ')
while True:
    x = input('Key: ')
    if x == 'end':
        break
    y = input('Value: ')
    if y == 'end':
        break
    
    dict2[x] = y
    
sorted(dict1.update(dict2))
for i in dict1:
    print('%s: %s' % (i, dict1[i]))