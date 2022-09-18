import math

x, y = eval(input())

if abs(0-x) <= (8/2) and abs(0-y) <= (6/2):
    print('(%d, %d) is inside of the rectangle' % (x, y))
else:
    print('(%d, %d) is outside of the rectangle' % (x, y))