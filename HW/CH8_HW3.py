
lst = []
for i in range(9):
    s = input()
    lst.append(s)
    
for i in range(9):
    print('|%-15s|' % lst[i], end = '')
    if (i+1) % 3 == 0 and i != 0:
        print()
