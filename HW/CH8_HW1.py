
while True:
    x = input()
    if x == 'end':
        break
    else:
        s = x.split(':')
        print('hour: %s, min : %s, second: %s'\
              %(s[0],s[1],s[2]))
