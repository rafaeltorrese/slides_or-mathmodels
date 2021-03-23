"""
Example 04-16
\min Z = 3x_1 + 2x_2 + x_3 + 4x_4
2x_1 + 4x_2 + 5x_3 + x_4 \geq 10
3x_1 - x_2 + 7x_3 - 2x_4 \geq 2
5x_1 + 2x_2 + x_3 +6x_4 \geq 1
"""

import numpy as np
np.set_printoptions(precision=3, suppress=True)

from dualsimplex_algorithm import dual_simplex
#%%
cj = np.array([-3, -2, -1, -4, 0, 0, 0] , dtype=float)

A = np.array([
    [-2, -4, -5, -1, 1, 0, 0],
    [-3,  1, -7,  2, 0, 1, 0],
    [-5, -2, -1, -6, 0, 0, 1],
    ] , dtype=float)

b = np.array([-10, -2, -15] , dtype=float)


#%%
soldualsimplex, gvalues, lastrow = dual_simplex(matrix=A,
                                  rhs=b,
                                  z=cj,
                                  numxvars=4)

print(20/23)