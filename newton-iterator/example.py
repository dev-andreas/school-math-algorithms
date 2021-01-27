import newton

def function(x):
    return x**2 - 5

def derivative(x):
    return 2*x

starting_pos = 4
iterations = 5

print(newton.find_zero(function, derivative, starting_pos, iterations=iterations))

print(newton.find_nth_root(3, 2))

