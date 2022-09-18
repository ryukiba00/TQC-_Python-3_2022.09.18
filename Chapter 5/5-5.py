def sumAndAverage(n1, n2):
    total = 0
    average = 0.0
    for i in range(n1, n2+1):
        total += i
    average = total/(n2-n1+1)
    return total, average

def main():
    s, a = sumAndAverage(1, 100)
    print('sum = %d, average = %2f'%(s, a))

main()