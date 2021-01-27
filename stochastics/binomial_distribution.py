from factorial import *

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
    Cumulative distribution function. (Gives the propability that a discrete random variable is not greater than some value)
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
