#%%
import numpy as np
import pandas as pd
#%%
def simplex(matrix, rhs, z, numxvars, direction=1):
    '''Simplex algorithm to solve linear programming problems

    Parameters
    ----------
    matrix: numpy ndarray
        Matrix of coefficients in the left-hand side in standard form

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
        Last rows of optimal table, this rows correspond to Zj and cj - Zj
    '''
    print("="*10, "Simplex Method", "="*10)

    matrix = np.array(matrix, dtype=float)
    rhs = np.array(rhs, dtype=float)
    z = np.array(z, dtype=float)

    num_rows, num_cols = matrix.shape

    onecols = np.where(matrix == 1)[1]
    cb_index = onecols[onecols >= numxvars]
    cb = z[cb_index]

    zj = cb.dot(matrix)

    net_evaluation = direction * (z - zj)

    solutions = []
    fvalues = []

    labels = [f"x{i + 1}" for i in range(num_cols)]

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

        print(f"Iteration {iteration}. {leaving_label} ---> {entering_label}")
        print(matrix,  "\n")
        print("Solution", solution, f"\tZ: {cb.dot(rhs):0.2f}")
        print(f'zj: {zj}')
        print(f'cj - zj: {net_evaluation}')
        print(f'rhs vector {direction * rhs}', "\n")

        solutions.append(solution)
        fvalues.append(cb.dot(rhs))
        if np.all(net_evaluation <= 0):
            print(f"Optimal solution found in {iteration} iterations")
            print((*zip(labels, np.round(solution, 3))))

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