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
    objfunc = np.array([-1, 2, -1, 0, 0, -1000, 0])

    A = np.array([
        [3,  1, -1, 1,  0, 0, 0],
        [-1,  4,  1, 0, -1, 1, 0],
        [0,  1,  1, 0,  0, 0, 1],
    ])

    B = np.array([10, 6, 4])

    nx = 3

    solutions, lastrows, table, rhs, cbindx = simplex(
        matrix=A, rhs=B, z=objfunc, numxvars=nx, direction=1)

    print(solutions, '\n')
    print(table, '\n')
    print(lastrows, '\n')
    print(rhs, '\n')

    Basis = A[:, cbindx]
    Binv = np.linalg.inv(Basis)
    print(Basis)
    print(Binv)

    # table.to_csv(r'F:\anahuac\Operations-Research\sensitivity\example01.csv')

    optimal_table = pd.concat([table, rhs], axis=1)
    print(optimal_table)
    # optimal_table.to_excel(
    #     r'F:\anahuac\Operations-Research\sensitivity\example_pandas01.xlsx')
