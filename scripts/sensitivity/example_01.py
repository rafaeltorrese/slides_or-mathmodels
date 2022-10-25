# %%
import numpy as np
import pandas as pd

from simplex_algorithm import simplex
from dualsimplex_algorithm import dual_simplex

from data import B
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

    
    B1 = np.array([7, 2])
    B2 = np.array([3, 9])

    

    solutions, lastrows, table, rhs, cbindx = simplex(
        matrix=A, rhs=B, obj_coef=objfunc, direction=1)

    print(solutions, '\n')
    print(table, '\n')
    print(lastrows, '\n')
    print(rhs, '\n')

    optimal_table = pd.concat([table, rhs], axis=1)
    print('\nOptimal Table')
    print(optimal_table)

    # optimal_table.to_excel(
    #     r'C:\Users\rafael.torrese\Documents\anahuac\2022-03_agu-dec\operations-research\example.xlsx'
    # )

    Basis = A[:, cbindx]
    Binv = np.linalg.inv(Basis)
    print(f'\nBase Matrix \n{Basis}')
    print(f'\nMatrix Inv Base \n{Binv}')

    print()
    new_solution = check_feasebility(Basis, B2)

    # table.to_csv(r'F:\anahuac\Operations-Research\sensitivity\example01.csv')

    
    
