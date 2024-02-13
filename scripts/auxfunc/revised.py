import numpy as np
import pandas as pd

def simplex(matrix, rhs, costs,  direction=1):
    '''Simplex algorithm to solve linear programming problems

    Parameters
    ----------
    matrix: numpy ndarray
        Matrix of coefficients in the left-hand side

    rhs: numpy ndarray
        Right-hand side vector

    numxvars: int
        Number of x variables

    direction: {+1 , -1}
        For maximization problems use +1 and for minimization problems use -1 instead.
    '''
    print("=======")

    matrix = np.array(matrix, dtype=float)
    rhs = np.array(rhs, dtype=float)
    costs = np.array(costs, dtype=float)

    num_rows, num_cols = matrix.shape

    
    cb_index = find_index_basics(matrix)
    cb = costs[cb_index]

    reduced_costs = cb.dot(matrix)


    net_evaluation = direction * (costs - reduced_costs)

    solutions = []
    fvalues = []

    # labels = [f"x{i + 1}" for i in range(num_cols)]

    iteration = 0
    while np.any(net_evaluation > 0):
        solution = np.zeros_like(costs)
        entering = net_evaluation.argmax()  # entering variables (index)
        # entering_label = labels[entering]

        key_col = matrix[:, entering]
        ratios = np.divide(rhs, key_col,
                           out=np.full_like(rhs, np.inf),
                           where=key_col > 0)

        leaving = ratios.argmin()   # leaving variables (index)
        # leaving_label = labels[cb_index[leaving]]

        print(cb_index)
        cb_index[leaving] = entering
        basis_matrix = matrix[:, cb_index]
        inverse_basis = np.linalg.inv(basis_matrix)

        simplex_matrix = inverse_basis.dot(matrix)
        simplex_rhs = inverse_basis.dot(rhs)

        cb = costs[cb_index]
        reduced_costs = cb.dot(matrix)
        net_evaluation = direction * (costs - reduced_costs)

        iteration += 1

        print(f"Iteration {iteration}. {leaving} ---> {entering}")
        print(simplex_matrix,  "\n")
        print("Solution", solution, f"\tZ: {cb.dot(rhs):0.2f}", "\n")

        solutions.append(solution)
        fvalues.append(cb.dot(rhs))
        if np.all(net_evaluation <= 0):
            print(f"Optimal solution found in {iteration} iterations")

    return np.array(solutions), fvalues, np.vstack((reduced_costs, net_evaluation))


def find_index_basics(A):
    filtered_matrix = np.where(A == 1, 1, np.divide(A, 1000)).sum(axis=0)
    mask = filtered_matrix == 1.0
    return np.nonzero(mask)[0]


if __name__ == '__main__':

    labels = np.array('x1 x2 x3 x4 s1 A1 s2 s3 A3 A3'.split())

    A = np.array([
        [3, 4, 8, 6, -1,  1,  0,  0, 0, 0],
        [2, 2, 7, 5,  0,  0, -1,  0, 1, 0],
        [6, 4, 7, 4,  0,  0,  0, -1, 0, 1],
    ], dtype=float)

    b = np.array([800, 200, 700])

    c = np.array([45, 40, 85, 65, 0,  0,  0,  1000, 1000, 1000])

    simplex(A, b, c,  direction=-1)
    
    
    