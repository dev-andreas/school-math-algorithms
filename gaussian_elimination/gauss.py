import numpy as np
import copy

testing_matrix = np.matrix('1 7 -1 5; 4 -1 1 1; 5 -3 1 -1')

def gauss(matrix: np.matrix, show=False) -> tuple:
    '''
    Gaussian elimination can solve linear equation systems of any size.
    Input should be a numpy matrix. There is a variable called
    'testing_matrix' already defined for demo purpose :)
    '''
    matrix_copy = copy.deepcopy(matrix)
    variables_amount = len(np.asarray(matrix_copy[0]).reshape(-1)) - 1
    
    if (variables_amount > len(matrix_copy)):
        raise Exception('Too much variables!')
        return None

    if show:
        print('starting matrix:')
        print(matrix_copy)

    for subtraction_index in range(variables_amount - 1):
        
        subtraction_matrix = matrix_copy[subtraction_index]
        
        for line in range(1 + subtraction_index, variables_amount):
            matrix_to_subtract = matrix_copy[line]
            matrix_copy[line] = matrix_to_subtract * subtraction_matrix[0, subtraction_index] - subtraction_matrix * matrix_to_subtract[0, subtraction_index]

        if show:
            print('iteration {}:'.format(subtraction_index))
            print(matrix_copy)

    solutions = np.array([])

    for equation in range(variables_amount - 1, -1, -1):
        addition = 0
        for variable, solution in zip(range(variables_amount - 1, equation, -1), solutions):
            addition += matrix_copy[equation, variable] * solution
 
        solutions = np.append(solutions, (matrix_copy[equation, variables_amount] - addition) / matrix_copy[equation, equation])
        
    solutions = np.flip(solutions)

    if show:
        print('\nsolutions set:\n{}'.format(solutions))

        print('\nsolutions:')
        for solution, index in zip(solutions, range(len(solutions))):
            print('x{i}: {s}'.format(s = solution, i = index))

    return tuple(solutions)
