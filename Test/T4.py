
lst = []
while True:
    x = int(input())
    
    if x == 9999:
        break
    else:
        lst.append(x)
        
print(min(lst))