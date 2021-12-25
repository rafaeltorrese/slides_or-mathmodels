# %%
import numpy as np
import pandas as pd

from simplex_algorithm import simplex
from dualsimplex_algorithm import dual_simplex
# %%


def check_feasebility(b, r):
    basis = np.linalg.inv(b)
    solution = basis.dot(r)
    print(f'Change to {r}')
    print(f'Results in Solution {solution}')
    if np.all(solution >= 0):
        print('Fasible Solution')
    else:
        print('Infeasible. Apply Dual Simplex')
    return solution


if __name__ == '__main__':
    objfunc = np.array([5, 12, 4, 0, -1000])

    A = np.array([
        [1,  2, 1, 1, 0],
        [2, -1, 3, 0, 1],
    ])

    B = np.array([5, 2])
    B1 = np.array([7, 2])
    B2 = np.array([3, 9])

    nx = 3

    solutions, lastrows, table, rhs, cbindx = simplex(
        matrix=A, rhs=B, z=objfunc, numxvars=nx, direction=1)

    print(solutions, '\n')
    print(table, '\n')
    print(lastrows, '\n')
    print(rhs, '\n')

    Basis = A[:, cbindx]
    Binv = np.linalg.inv(Basis)
    print(Basis, '\n')
    print(Binv, '\n')

    new_solution = check_feasebility(Basis, B2)

    # table.to_csv(r'F:\anahuac\Operations-Research\sensitivity\example01.csv')

    optimal_table = pd.concat([table, rhs], axis=1)
    print(optimal_table)
    # optimal_table.to_excel(
    #     r'F:\anahuac\Operations-Research\sensitivity\example_pandas01.xlsx')
