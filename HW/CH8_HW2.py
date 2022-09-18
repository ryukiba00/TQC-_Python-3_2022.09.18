
s = input()

count = 0
if not s[0].isalpha():
    count += 1
    print('Invalid variable name')

for i in range(1,len(s)):
    if not s[i].isalnum():
        count += 1
        print('Invalid variable name')
        break

if count == 0:
    print('Valid variable name')
    