import numpy as np
import pandas as pd


def simplex(matrix, rhs, z, numxvars, varlabel='x', direction=1):
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
        Use +1 for maximization and -1 for minimization.

    Returns
    -------
    solutions: numpy ndarray
        Vector solutions of every iteration

    fvalues: numpy ndarray
        Values of z (objective function)

    lastrows: numpy ndarray
        Last rows of optimal table, this rows corresponde to Zj and cj - Zj
    '''
    print("="*10, "Simplex Method", "="*10)

    matrix = np.array(matrix, dtype=float)
    rhs = np.array(rhs, dtype=float)
    z = np.array(z, dtype=float)

    num_rows, num_cols = matrix.shape

    onecols = np.where(matrix == 1 & (np.abs(matrix).sum(axis=0) == 1))[1]
    cb_index = onecols[onecols >= numxvars]
    cb = z[cb_index]

    zj = cb.dot(matrix)

    net_evaluation = direction * (z - zj)

    solutions = []
    fvalues = []

    labels = [f"{varlabel}{i + 1}" for i in range(num_cols)]
    basis = [labels[i] for i in cb_index]

    iteration = 0
    while np.any(net_evaluation > 0):
        solution = np.zeros_like(z)
        entering = net_evaluation.argmax()  # entering variables (index)
        entering_label = labels[entering]

        key_col = matrix[:, entering]

        ratios = np.divide(rhs, key_col,
                           out=np.full_like(rhs, np.inf),
                           where=key_col > 0)

        leaving = ratios.argmin()   # leaving variables (index)
        leaving_label = labels[cb_index[leaving]]
        # ==================
        pivot = matrix[leaving, entering]

        if pivot != 1:
            matrix[leaving] = matrix[leaving] / pivot
            rhs[leaving] = rhs[leaving] / pivot

        for i in range(num_rows):
            if i != leaving:
                factor = matrix[i, entering]
                matrix[i] = -factor * matrix[leaving] + matrix[i]
                rhs[i] = -factor * rhs[leaving] + rhs[i]
        # ==================
        cb_index[leaving] = entering

        cb = z[cb_index]
        zj = cb.dot(matrix)
        net_evaluation = direction * (z - zj)

        solution[cb_index] = rhs  # basics

        iteration += 1
        basis[leaving] = entering_label
        print(f'Iteration {iteration}. {leaving_label} ---> {entering_label}')
        print(matrix,  "\n")
        print(f'Solution {solution} \t Z: {cb.dot(rhs):0.2f}')
        print(f'cj - zj: {net_evaluation}')
        print(f'rhs vector {direction * rhs}', "\n")

        solutions.append(solution)
        fvalues.append(cb.dot(rhs))
        if np.all(net_evaluation <= 0):
            print(f"Optimal solution found in {iteration} iterations")
            # print((*zip(labels, np.round(solution, 3))))

            print()
            return pd.DataFrame(np.array(solutions), index=[f'iter{str(i).zfill(2)}' for i in range(1, iteration + 1)], columns=labels),  pd.DataFrame(np.vstack((zj, net_evaluation)), index=['zj', 'cj - zj'], columns=labels), pd.DataFrame(matrix, columns=labels, index=basis), pd.Series(rhs, index=basis), cb_index


if __name__ == '__main__':
    Aprimal = [
        [6, 4, 1, 0, 0, 0],
        [1, 2, 0, 1, 0, 0],
        [-1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1],
    ]

    bprimal = [24, 6, 1, 2]

    Zvector = [5, 4, 0, 0, 0, 0]

    nvars = 2

    sols, lastrows, table, bsolution, cbindx = simplex(matrix=Aprimal, rhs=bprimal,
                                                       z=Zvector, numxvars=nvars,  direction=1)

    print(sols.loc['iter02'])
