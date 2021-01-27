def find_zero(function, derivative, start, iterations=10):
    '''Finding zeroes of a function.'''
    position = start
    for i in range(iterations):
        position -= function(position) / derivative(position)
    return position

def find_nth_root(number, exponent, iterations=10):
    '''Finding the nth root of a number'''
    def function(x):
        return x**exponent - number
    def derivative(x):
        return exponent * x**(exponent-1)

    return find_zero(function, derivative, 1, iterations=iterations)
