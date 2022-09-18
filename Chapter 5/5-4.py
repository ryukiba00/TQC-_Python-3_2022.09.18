def total(a,b):
    sum = 0
    for i in range(a, b+1):
        sum += i
    return sum

def main():
    x = eval(input('Enter start number: '))
    y = eval(input('Enter end number: '))
    t = total(x, y)
    print('summation of %d to %d: %d'%(x, y, t))

main()