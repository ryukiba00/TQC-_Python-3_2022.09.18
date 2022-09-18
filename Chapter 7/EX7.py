
setX = set()
print('Enter group X\'s subjects: ')
while True:
    x = input()
    if x == 'end':
        break
    else:
        setX.add(x)

setY = set()
print('Enter group Y\'s subjects: ')
while True:
    x = input()
    if x == 'end':
        break
    else:
        setY.add(x)
        
print(sorted(setX|setY))
print(sorted(setX&setY))
print(sorted(setY-setX))
print(sorted(setX^setY))