"""
$$\min Z = -4x_1 + x_2 + 2x_3$$

\begin{align*}
2x_1 - 3x_2 + 2x_3 &  \leq  12\\
-5x_1 + 2x_2 + 3x_3 & \geq 4\\
3x_1 - 2x_3& = -1\\[5mm]
x_1, x_2, x_3 & \geq 0
\end{align*}
"""
import numpy as np
np.set_printoptions(precision=3, suppress=True)

from auxfunc.simplex_algorithm import simplex
from auxfunc.simplex_revised import simplex_revised


cj = [-4, 1, 2, 0, 0, 1000, 1000]

A = [
    [ 2, -3, 2, 1,  0, 0, 0],
    [-5,  2, 3, 0, -1, 1, 0],
    [-3,  0, 2, 0,  0, 0, 1],
]

b = [12, 4, 1]


solutions_primal, zvalues, lastrows_z = simplex(matrix=A, rhs=b, z=cj, numxvars=3, direction=-1)

solutions_primal, zvalues, lastrows_z = simplex_revised(matrix=A, rhs=b, z=cj, numxvars=3, direction=-1)


