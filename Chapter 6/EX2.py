
list1 = []
sum1 = 0
for i in range(0, 5):
    x = input()
    list1.append(x)
    if list1[i] == 'J':
        x = 11
    elif list1[i] == 'Q':
        x = 12
    elif list1[i] == 'K':
        x = 13
    elif list1[i] == 'A':
        x = 1
    sum1 += x 

print(sum1)