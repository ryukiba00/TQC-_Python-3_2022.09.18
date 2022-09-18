
set1 = set()
while True:
    x = int(input())
    if x == -9999:
        break
    else:
        set1.add(x)

print('Length: ', len(set1))
print('Max: ', max(set1))
print('Min: ', min(set1))
print('Sum: ',sum(set1))