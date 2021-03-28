"""
Example 04-15

\min Z = x_1 + x_2

      2x_1 + x_2 \geq 2
      -x_1 - x_2 \geq 1
"""

import numpy as np
from dualsimplex_algorithm import dual_simplex


cj = np.array([-1, -1, 0, 0] , dtype=float)

A = np.array([
    [-2, -1, 1, 0],
    [ 1,  1, 0, 1],
    ] , dtype=float)

b = np.array([-2, -1] , dtype=float)


#%%
soldualsimplex, gvalues, lastrow = dual_simplex(matrix=A,
                                  rhs=b,
                                  z=cj,
                                  numxvars=2)