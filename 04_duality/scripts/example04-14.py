"""
\max Z = 3x_1 + 4x_2 \]

5x_1 + 4x_2 \leq 200
3x_1 + 5x_2 \leq 150
5x_1 + 4x_2 \geq 100
8x_1 + 4x_2 \geq 80
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