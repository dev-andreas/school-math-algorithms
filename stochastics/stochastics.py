def factorial(x: int) -> int:
    ''' Calculates n-factorial (n!) '''
    y = 1
    for z in range(1,x):
        y *= z+1
    return y


def bincoef(n: int, k: int) -> int:
    ''' Binomial coefficient function "n choose k" '''
    return factorial(n)/(factorial(k)*factorial(n-k))  


def pmf(k: int, n: int, p: float) -> float:
    ''' 
    Probability mass function. (Gives the propability that a discrete random variable is exactly equal to some value)
    '''
    return bincoef(n, k)*(p)**k*(1-p)**(n-k)


def map_pmf(k: tuple, n: int, p: float) -> tuple:
    '''
    Probability mass function. (Gives the propability that a discrete random variable is exactly equal to some value)
    Takes tuple as first argument
    '''
    pmf_function = lambda x: pmf(x, n, p)
    return tuple(map(pmf_function, k))


def cdf(k: int, n: int, p: float) -> float:
    '''
    Cumulative distribution function. (Gives the propability that a discrete random variable is not greater than some value)
    '''
    return sum(map_pmf(range(k+1), n, p))


def map_cdf(k: tuple, n: int, p: float) -> tuple:
    '''
    Cumulative distribution function. (Gives the propability that a discrete random variable is not greater than some value)
    Takes tuple as first argument
    '''
    cdf_function = lambda x: cdf(x, n, p)
    return tuple(map(cdf_function, k))

def expected_value(values: tuple) -> float:
    '''
    Calculates the expected value of a values tuple e.g. ((value 1, probability 1), ..., (value n, probability n))
    '''
    function = lambda value: value[0] * value[1]
    return sum(map(function, values))

def standard_deviation(values: tuple) -> float:
    '''
    Calculates the standard deviation of a values tuple e.g. ((value 1, probability 1), ..., (value n, probability n))
    '''
    my = expected_value(values)
    sigma_function = lambda value: (value[0] - my)**2 * value[1]
    return sum(map(sigma_function, values))**(1/2)
