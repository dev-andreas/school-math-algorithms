def factorial(x):
    ''' Calculates n-factorial (n!) '''
    y = 1
    for z in range(1,x):
        y *= z+1
    return y


factorial(3)


