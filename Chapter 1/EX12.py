import math

x1, y1 = eval(input())
x2, y2 = eval(input())
x3, y3 = eval(input())

side1 = math.sqrt((x2-x1)**2+(y2-y1)**2)
side2 = math.sqrt((x3-x2)**2+(y3-y2)**2)
side3 = math.sqrt((x3-x1)**2+(y3-y1)**2)

s = (side1+side2+side3)/2
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))

print('The area of the triangle = %.2f' % area)