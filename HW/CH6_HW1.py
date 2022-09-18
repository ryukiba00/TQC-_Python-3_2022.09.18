def add(lst1, lst2):
    lst3 = []
    for i in range(2):
        lst3.append([])
        for j in range(2):
            lst3[i].append(lst1[i][j] + lst2[i][j])
            
    return lst3


def show(lst1, lst2, lst3):
    print('Matrix 1')
    for i in range(2):
        for j in range(2):
            print('%3d'%lst1[i][j], end = '')
        print()
        
    print('Matrix 2')
    for i in range(2):
        for j in range(2):
            print('%3d'%lst2[i][j], end = '')
        print()
    
    print('Sum of matrices')
    for i in range(2):
        for j in range(2):
            print('%3d'%(lst3[i][j]), end = '')
        print()

def main():
    matrix1 = []
    matrix2 = []
    
    print('Enter matrix1:')
    for i in range(2):
        matrix1.append([])
        for j in range(2):
            matrix1[i].append(eval(input('[%d %d]: '%(i+1,j+1))))
            #matrix1[i] = eval(input('[%d %d]: '%(i+1,j+1)))
    
    print('Enter matrix2:')
    for i in range(2):
        matrix2.append([])
        for j in range(2):
            matrix2[i].append(eval(input('[%d %d]: '%(i+1,j+1))))
            #matrix2[i] = eval(input('[%d %d]: '%(i+1,j+1)))
            
    matrix3 = add(matrix1, matrix2)
    show(matrix1, matrix2, matrix3)
    
main()