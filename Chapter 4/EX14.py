
a = int(input())

i = 2
while i < a:
    if a % i == 0:
        print('%d is not a prime number.' % a)
        break
    else:
        i += 1
        if i == a:
            print('%d is a prime number.' % a)
