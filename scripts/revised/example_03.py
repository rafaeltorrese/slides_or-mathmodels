"""
$$\max Z = x_1 + 2x_2 + 3x_3 - x_4$$

\begin{align*}
x_1 + 2x_2 + 3x_3 &=  15\\
2x_1 + x_2 + 5x_3 & = 20\\
x_1 + 2x_2 + x_3 + x_4 & = 10\\[5mm]
x_1, x_2, x_3, x_4 & \geq 0
\end{align*}
"""
import numpy as np
np.set_printoptions(precision=3, suppress=True)

from auxfunc.simplex_algorithm import simplex
from auxfunc.simplex_revised import simplex_revised


cj = [1, 2, 3, -1, -10000, -10000]

A = [
    [1, 2, 3, 0, 1, 0],
    [2, 1, 5, 0, 0, 1],
    [1, 2, 1, 1, 0, 0],
]

b = [15, 20, 10]


# solutions_primal, zvalues, lastrows_z = simplex(matrix=A, rhs=b, z=cj, numxvars=3)

solutions_primal, zvalues, lastrows_z = simplex_revised(matrix=A, rhs=b, z=cj, numxvars=3)


