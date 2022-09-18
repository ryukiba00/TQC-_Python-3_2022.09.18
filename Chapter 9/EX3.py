
file = open('data.txt', 'a+')
for i in range(5):
    data = input()
    file.write('\n'+data)

print('Append compeleted!')
print('Content of "data.txt": ')
file.seek(0, 0)
print(file.read())

file.close()