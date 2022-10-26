import numpy as np
import pandas as pd

from data import A, b, z

def simplex(matrix, rhs, obj_coef,  varlabel='x', direction=1):
    '''Simplex algorithm to solve linear programming problems

    Parameters
    ----------
    matrix: numpy ndarray
        Matrix of coefficients in the left-hand side

    rhs: numpy ndarray
        Right-hand side vector


    direction: {+1 , -1}
        Use +1 for maximization and -1 for minimization.

    Returns
    -------
    solutions: pandas DataFrame
        Vector solutions of every iteration

    lastrows: pandas DataFrame
        Last rows of optimal table, this rows corresponde to Zj and cj - Zj

    table: pandas DataFrame
        Optimal Simplex Table

    rhs: pandas DataFrame
        RHS values in the Optimal Simplex Table

    cb_index: numpy ndarray
        index of entering variables regarding to labels
    '''
    print("="*10, "Simplex Method", "="*10)

    matrix = np.array(matrix, dtype=float)
    rhs = np.array(rhs, dtype=float)
    obj_coef = np.array(obj_coef, dtype=float)

    num_rows, num_cols = matrix.shape

    # cb_index = np.where((matrix == 1) & (np.abs(matrix).sum(axis=0) == 1))[1]
    cb_index = np.where((matrix == 1) & (np.abs(matrix).sum(axis=0) == 1))[1]
    
    cb = obj_coef[cb_index]
    zj = cb.dot(matrix)

    net_evaluation = direction * (obj_coef - zj)

    solutions = []
    fvalues = []

    labels = [f"{varlabel}{i + 1}" for i in range(num_cols)]
    basis = [labels[i] for i in cb_index]

    iteration = 0
    while np.any(net_evaluation > 0):
        solution = np.zeros_like(obj_coef)
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

        cb = obj_coef[cb_index]
        zj = cb.dot(matrix)
        net_evaluation = direction * (obj_coef - zj)

        solution[cb_index] = rhs  # basics

        iteration += 1
        basis[leaving] = entering_label
        print(f'Iteration {iteration}. {leaving_label} ---> {entering_label}')
        print(matrix,  "\n")
        # print(f'Solution {solution} \t Z: {cb.dot(rhs):0.2f}')
        # print(f'cj - zj: {net_evaluation}')
        # print(f'rhs vector {direction * rhs}', "\n")

        solutions.append(solution)
        fvalues.append(cb.dot(rhs))
        if np.all(net_evaluation <= 0):
            zvalue = cb.dot(rhs)
            print(f"Optimal solution found in {iteration} iterations")
            print(f'Z value: {zvalue}')

            return (
                pd.DataFrame(np.array(solutions), index=[f'iter{str(i).zfill(2)}' for i in range(1, iteration + 1)], columns=labels),  # solutions
                pd.DataFrame(np.vstack((direction * zj, direction * net_evaluation)), index=['zj', 'cj - zj'], columns=labels),  # last rows
                pd.DataFrame(matrix, columns=labels, index=basis),  # optimal body table
                pd.Series(rhs, index=basis,  name='solution'),  # optimal solution
                cb_index,  # index basic solution
                )


if __name__ == '__main__':
    sols, lastrows, table, bsolution, cbindx = simplex(matrix=A, rhs=b,
                                                       obj_coef=z,   direction=-1)

    print(f'Optimal solution \n{bsolution}\n')
    
    optimal_table = pd.concat([table, bsolution], axis=1)
    print('\nOptimal Table')
    print(optimal_table)

    optimal_table.to_excel(
        r'C:\Users\rafael.torrese\Documents\anahuac\2022-03_agu-dec\operations-research\example2.xlsx'
    )

    
