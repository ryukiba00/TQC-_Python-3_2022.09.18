def total():
    sum = 0
    for i in range(1, 101):
        sum += i
    return sum

def main():
    t = total()
    print('summation of 1 to 100:', t)

main()