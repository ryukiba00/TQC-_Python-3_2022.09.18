
total = 0
for i in range(5):
    x = input()
    if x == 'J':
        total += 11
    elif x == 'Q':
        total += 12
    elif x == 'K':
        total += 13
    elif x == 'A':
        total += 1
    else:
        total += int(x)
        
print(total)