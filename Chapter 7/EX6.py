
k = int(input())
for i in range(0, k):
    set1 = set()
    x = input()
    set1.add(x)
    set1.remove(' ')
    
print(len(set1) == 26)