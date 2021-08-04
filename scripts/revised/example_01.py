"""
$$\max Z = 6x_1 + 3x_2 + 4x_3 - 2x_4 + x_5$$

\begin{align*}
2x_1 + 3x_2 + 3x_3 + x_4 & = 10\\
x_1 + 2x_2 + x_3 + x_5 & = 8\\[5mm]
x_1, x_2, x_3, x_4, x_5 & \geq 0
\end{align*}
"""
import numpy as np
np.set_printoptions(precision=3, suppress=True)

from auxfunc.simplex_algorithm import simplex
from auxfunc.simplex_revised import simplex_revised


cj = np.array([6, 3, 4, -2, 1])

A = np.array([
    [2, 3, 3, 1, 0],
    [1, 2, 1, 0, 1],
])

b = np.array([10, 8])


solutions_primal, zvalues, lastrows_z = simplex_revised(matrix=A, rhs=b, z=cj, numxvars=3)
