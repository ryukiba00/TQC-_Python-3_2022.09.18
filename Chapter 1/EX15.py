n = eval(input('Enter monthly saving amount: '))

i = 1
while(i<= 6):
    n *= (1+0.001025)
    i+=1

print('After the sith month, the account value is %.2f'%n)