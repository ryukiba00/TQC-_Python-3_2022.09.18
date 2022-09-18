
tuple1 = ()
print('Create tuple1:')
while True:
    x = int(input())
    if x == -9999:
        break
    else:
        tuple1 += (x, )

tuple2 = ()
print('Create tuple2:')
while True:
    x = int(input())
    if x == -9999:
        break
    else:
        tuple2 += (x, )
        
print('Combined tuple before sorting: ', (tuple1+tuple2))
print('Combined list after sorting: ', sorted(list(tuple1+tuple2)))
