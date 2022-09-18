
n = eval(input())

i = 1
pay = n
while pay < (n * 2):
    pay += (pay * 3 / 100)
    print('#%d year: %.2f' % (i, pay))
    
    i += 1
    
print('Tuition will be doubled in %d year' % (i-1))