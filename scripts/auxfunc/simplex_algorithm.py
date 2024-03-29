#%%
import numpy as np
import pandas as pd
<<<<<<< HEAD
#%%
def simplex(matrix, rhs, z, numxvars, direction=1):
=======


def simplex(matrix, rhs, z, direction=1):
>>>>>>> c07e6c4f2b46a6747ca4b089fb0e0f54f5fb12a9
    '''Simplex algorithm to solve linear programming problems

    Parameters
    ----------
    matrix: numpy ndarray
        Matrix of coefficients in the left-hand side in standard form

    rhs: numpy ndarray
        Right-hand side vector

    direction: {+1 , -1}
        Use +1 for maximization and -1 for minimization.

    Returns
    -------
    solutions: numpy ndarray
        Vector solutions of every iteration

    fvalues: numpy ndarray
        Values of z (objective function)

    lastrows: numpy ndarray
        Last rows of optimal table, this rows correspond to Zj and cj - Zj
    '''
    print("="*10, "Simplex Method", "="*10)

    matrix = np.array(matrix, dtype=float)
    rhs = np.array(rhs, dtype=float)
    z = np.array(z, dtype=float)

    num_rows, num_cols = matrix.shape

    cb_index = np.where(matrix.sum(axis=0) == 1)[0]
    cb = z[cb_index]

    zj = cb.dot(matrix)

    net_evaluation = direction * (z - zj)

    labels = [f"x{i + 1}" for i in range(num_cols)]
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
<<<<<<< HEAD
        print("Solution", solution, f"\tZ: {cb.dot(rhs):0.2f}")
        print(f'zj: {zj}')
=======
        print(f'Solution {solution} \t Z: {cb.dot(rhs):0.2f}')
>>>>>>> c07e6c4f2b46a6747ca4b089fb0e0f54f5fb12a9
        print(f'cj - zj: {net_evaluation}')
        print(f'rhs vector {direction * rhs}', "\n")

        if np.all(net_evaluation <= 0):
            print(f"Optimal solution found in {iteration} iterations")
            print((*zip(labels, np.round(solution, 3))))
            print(basis)
            print()

    return pd.DataFrame(np.vstack((zj, net_evaluation)), index=['zj', 'cj - zj'], columns=labels), pd.DataFrame(matrix, index=basis, columns=labels)


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

    lastrows, table = simplex(matrix=Aprimal, rhs=bprimal,
                              z=Zvector, direction=1)

<<<<<<< HEAD
    return pd.DataFrame(np.array(solutions), index=range(1, interation + 1), columns=labels), pd.DataFrame(np.vstack((zj, net_evaluation)), index=['zj', 'cj - zj'], columns=labels)
#%%
if __name__ == '__main__':
    LHS = np.array([
    [1,  2],
    [1,  1],
    [1, -1],
    [1, -2],
])

nconstraints, nvars = LHS.shape  # number of variables, only x variables

I = np.eye(LHS.shape[0])
print(I)
M = np.hstack((LHS, I))
print(A)

B = np.array([10, 6, 2, 1])

Z = np.array([2, 1])

simplex(matrix=M, rhs=B, z=np.concatenate((Z, [0] * nconstraints)), numxvars=nvars, direction=1)
#%%
=======
    print(table)
>>>>>>> c07e6c4f2b46a6747ca4b089fb0e0f54f5fb12a9
