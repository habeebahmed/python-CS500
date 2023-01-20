def divide(x, y):
    q = x // y
    r = x % y
    return q, r
    
def main():
    num = (6, 5, 7)

    #num.append(8)        # AttributeError: 'tuple' object has no attribute 'append'
    #num.sort()           # AttributeError: 'tuple' object has no attribute 'sort'
    #num[0] = 10          # TypeError: 'tuple' object does not support item assignment
    print('num =', num)
    print('num[1:3]', num[1:3])
    
    x, y, z = num
    print('x =', x)
    print('y =', y)
    print('z =', z)
        
    quotient, remainder = divide(5, 2)
    print('quotient =', quotient)
    print('remainder =', remainder)
    
if __name__ == "__main__":
    main()
    
