
dct = {}
while True:
    x = int(input('Input key: '))
    if x == -9999:
        print('Input value: -9999')
        break
    y = input('Input value: ')
    dct[x] = y
    
print(dct)

x = int(input('Which key do you want to delete: '))
if x not in dct:
    print('not found')
else:
    del dct[x]
    print(dct)