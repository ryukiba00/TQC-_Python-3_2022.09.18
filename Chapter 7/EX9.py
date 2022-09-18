

color_dict = {}
while True:
    x = input('Key: ')
    if x == 'end':
        break
    y = input('Value: ')
    if y == 'end':
        break
    
    color_dict[x] = y

sorted(color_dict)
for i in color_dict:
    print('%s :%s' % (i, color_dict[i]))