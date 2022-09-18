
dct = {}
while True:
    print('1: add\n\
2: delete\n\
3: query\n\
4: display\n\
5: exit')

    a = int(input('Which one: '))
    # a為1, add
    if a == 1:
        b = int(input('Input key: '))
        if b in dct:
            print('the key is already existed.')
        else:
            c = input('Input value: ')
            dct[b] = c
    # a為2, delete
    elif a == 2:
        b = int(input('Input key: '))
        if b not in dct:
            print('the key is not found.')
        else:
            dct.pop(b)
            print('%d has been deleted'% b)
    # a為3, query
    elif a == 3:
        if b not in dct:
            print('the key is not found.')
        else:
            b = int(input('Input key: '))
            print(dct.get(b))
    # a為4, display
    elif a == 4:
        for i in dct:
            print('%d:%s'%(i,dct[i]))
    # a為5, exit
    elif a == 5:
        break
    # a為其他數字
    else:
        print('Try again')