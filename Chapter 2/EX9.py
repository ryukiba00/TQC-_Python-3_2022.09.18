import math

x = eval(input())
y = eval(input())

dis = math.sqrt((5-x)**2 + (6-y)**2)

if dis <= 15:
    print('Inside')
else:
    print('Outside')