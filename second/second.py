
import math as m

def fff(a,d):

    return a+d
def ddd(a,d):
    return a**d
def mmm(a,d):
    return m.sin(a*d)

if __name__ == '__main__':
    print(fff(2,2))
    print(ddd(2222,2))
    print(mmm(3,2))
    print(list(map(fff, [1,2,3,4,1], [4,6,8,9,0,8])))