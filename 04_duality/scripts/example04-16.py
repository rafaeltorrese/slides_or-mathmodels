"""
Example 04-16
\min Z = 3x_1 + 2x_2 + x_3 + 4x_4
2x_1 + 4x_2 + 5x_3 + x_4 \geq 10
3x_1 - x_2 + 7x_3 - 2x_4 \geq 2
5x_1 + 2x_2 + x_3 +6x_4 \geq 1
"""

import numpy as np

from dualsimplex_algorithm import dual_simplex
#%%
cj = np.array([3, 4, 0, 0, 0, 0] , dtype=float)

A = np.array([
    [ 5,  4, 1, 0, 0, 0],
    [ 3,  5, 0, 1, 0, 0],
    [-5, -4, 0, 0, 1, 0],
    [-8, -4, 0, 0, 0, 1]
    ] , dtype=float)

b = np.array([200, 150, -100, -80] , dtype=float)


#%%
soldualsimplex, gvalues, lastrow = dual_simplex(matrix=A,
                                  rhs=b,
                                  z=cj,
                                  numxvars=2)