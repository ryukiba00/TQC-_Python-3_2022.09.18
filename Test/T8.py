

s = input()

total = 0
for i in range(len(s)):
    print('ASCII code for \'%s\' is %d' % (s[i], int(ord(s[i]))))
    total += int(ord(s[i]))

print(total)