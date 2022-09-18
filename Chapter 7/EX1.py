
tuple1 = ()
while True:
    x = int(input())
    if x == -9999:
        break
    else:
        tuple1 += (x, )
    
print(tuple1)
print('Length: ',len(tuple1))
print('Max: ',max(tuple1))
print('Min: ',min(tuple1))
print('Sum: ',sum(tuple1))