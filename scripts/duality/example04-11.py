"""
Example 04-11

\min Z = 2x_1 + 2x_2 + 4x_3

2x_1 + 3x_2 + 5x_3 \geq 2
3x_1 + x_2 + 7x_3  \leq 3
x_1 + 4x_2 + 6x_3  \leq 5

"""

import numpy as np
np.set_printoptions(precision=3, suppress=True)

from dualsimplex_algorithm import dual_simplex
#%%

cj = np.array([-2, -2, -4, 0, 0, 0], dtype=float)

A = np.array([
    [-2, -3, -5,  1, 0, 0],
    [ 3,  1,  7,  0, 1, 0],
    [ 1,  4,  6,  0, 0, 1],
    ], dtype=float)

b = np.array([-2, 3, 5], dtype=float)
#%%
solutions, zvalues, lastrow = dual_simplex(matrix=A,
                                  rhs=b,
                                  z=cj,
                                  numxvars=3)

print(solutions, zvalues)


