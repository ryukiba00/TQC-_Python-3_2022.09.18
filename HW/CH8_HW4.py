
lst = [] 
while True:
    x = input()
    if x[-1] == 'e':
        lst.append(x)
    elif x == 'end':
        break

print(lst)