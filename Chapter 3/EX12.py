
print('華氏\t 攝氏')

for i in range(10, 241, 10):
    print('%-d\t %.2f' % (i, (5 / 9 *(i-32) )))