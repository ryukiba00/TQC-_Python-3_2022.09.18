

file = open('scores.dat', 'w')
while True:
    x = input()
    y = int(input())
    
    if x == 'none':
        break
    else:
        file.write(x+' '+str(y)+'\n')
    
file.close()