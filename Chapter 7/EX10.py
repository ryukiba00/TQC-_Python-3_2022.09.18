

dict1 = {}
while True:
    x = input('Key: ')
    if x == 'end':
        break
    y = input('Value: ')
    if y == 'end':
        break
    
    dict1[x] = y

x = input('Search key: ')
print(x in dict1)