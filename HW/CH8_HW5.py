

s = input()
for i in range(len(s)):
    if s[i].isalpha():
        if s[i].isupper():
            print('%s: is upper alpha.' % s[i])
        else:
            print('%s: is lower alpha.' % s[i])
    elif s[i].isdigit():
        print('%s: is number.' % s[i])
    elif s[i].isspace():
        print('%s: is a space.' % s[i])
    else:
        print('%s is a symbol character.' % s[i])