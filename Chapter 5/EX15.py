import math

def nEdge(x, y):
    return (x*(y**2))/(4*math.tan(math.pi/x))

def main():
    n = int(input())
    g = eval(input())
    
    print('area = %.2f' % nEdge(n, g))

main()