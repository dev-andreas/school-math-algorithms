
def fac(x: int) -> int:
    ''' Calculates n-factorial (n!) '''
    y = 1
    for z in range(1,x):
        y *= z+1
    return y
