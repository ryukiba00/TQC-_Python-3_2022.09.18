
file = open('friends.dat','w')
for i in range(5):
    data = input()
    file.write(data+'\n')
    
file.close()
    