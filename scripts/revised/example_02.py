"""
$$\max Z = 2x_1 + x_2$$

\begin{align*}
3x_1 + 4x_2 &\leq  6\\
6x_1 + x_2  & \leq 3\\[5mm]
x_1, x_2 & \geq 0
\end{align*}
"""
import numpy as np
np.set_printoptions(precision=3, suppress=True)

from auxfunc.simplex_algorithm import simplex
from auxfunc.simplex_revised import simplex_revised


cj = [2, 1, 0, 0]

A = [
    [3, 4, 1, 0],
    [6, 1, 0, 1],
]

b = [6, 3]


solutions_primal, zvalues, lastrows_z = simplex(matrix=A, rhs=b, z=cj, numxvars=2)

solutions_primal, zvalues, lastrows_z = simplex_revised(matrix=A, rhs=b, z=cj, numxvars=2)


