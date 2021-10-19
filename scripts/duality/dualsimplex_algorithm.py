import numpy as np
import pandas as pd


def dual_simplex(matrix, rhs, z, numxvars, varlabel='x'):
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
    matrix = np.array(matrix, dtype=float)
    rhs = np.array(rhs, dtype=float)
    z = np.array(z, dtype=float)

    num_rows, num_cols = matrix.shape

    onecols = np.where(matrix == 1 & (np.abs(matrix).sum(axis=0) == 1))[1]
    cb_index = onecols[onecols >= numxvars]
    cb = z[cb_index]

    zj = cb.dot(matrix)

    net_evaluation = z - zj

    solutions = []

    labels = [f"{varlabel}{i + 1}" for i in range(num_cols)]

    iteration = 0
    if np.any(net_evaluation > 0):
        print("Method Fails")
        print(f'Net Evaluation Row {net_evaluation}')
        return
    while np.all(net_evaluation <= 0) and np.any(rhs < 0):
        solution = np.zeros_like(z)

        leaving = rhs.argmin()   # leaving variables (index)
        key_row = matrix[leaving]

        if np.all(key_row >= 0):
            print("Infeasible Solution")
            return

        ratios = np.divide(net_evaluation, key_row,
                           out=np.full_like(z, np.inf), where=key_row < 0)

        entering = ratios.argmin()

        pivot = matrix[leaving, entering]

        if pivot != 1:
            matrix[leaving] = np.divide(matrix[leaving], pivot)
            rhs[leaving] = np.divide(rhs[leaving], pivot)

        for i in range(num_rows):
            if i == leaving:
                continue
            factor = matrix[i, entering]
            matrix[i] = -factor * matrix[leaving] + matrix[i]
            rhs[i] = -factor * rhs[leaving] + rhs[i]

        cb_index[leaving] = entering

        cb = z[cb_index]
        zj = cb.dot(matrix)
        net_evaluation = z - zj

        solution[cb_index] = rhs  # basics

        iteration += 1

        print(f"Iteration {iteration}")
        print(matrix,  "\n")
        print(f'Solution {solution} \t Z: {cb.dot(rhs):0.2f} \n')

        solutions.append(solution)

        if np.any(net_evaluation > 0):
            print("Method Fails")
            return

        if np.all(net_evaluation <= 0) and np.all(rhs >= 0):
            print(f"Optimal solution found in {iteration} iterations")

    return pd.DataFrame(matrix, columns=labels), pd.DataFrame(np.vstack((zj, net_evaluation)), index=['zj', 'cj - zj'], columns=labels)


if __name__ == '__main__':

    A = [
        [-6, -1,  1,  0, 1,	0],
        [-4, -2, -1, -1, 0,	1],
    ]

    b = [-5, -4]

    Z = [-24, -6, -1, -2, 0, 0]

    table, lastrows = dual_simplex(matrix=A, rhs=b, z=Z, numxvars=4)

    print(table)
