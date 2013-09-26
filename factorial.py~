
#from factorial import factorial

def factorial(n):
    import math
    if not n >= 0:
        raise ValueError('n must be >=0')
    if math.floor(n) != n:
        raise ValueError('n must be integer')
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor +=1
        # i.e. 4! = 1*2*3*4
    return result
