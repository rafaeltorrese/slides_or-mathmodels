'''
Example 03-36

$$\min Z = 45x_1 + 40x_2 + 85x_3 + 65x_4 $$

\begin{align*}
3x_1 + 4x_2 +  8x_3  + 6x_4 & \geq 800\\
2x_1 + 2x_2 +  7x_3  + 5x_4 & \geq 200\\
6x_1 + 4x_2 +  7x_3 + 4x_4 & \geq 700\\[5mm]
x_1, x_2,x_3, x_4 & \geq 0
\end{align*}
'''
from pprint import pprint
import numpy as np
np.set_printoptions(precision=3, suppress=True)

from auxfunc.simplex_algorithm import simplex
from auxfunc.twophase_method import twophase

cj = np.array([45, 40, 85, 65, 0, 0, 0, 1000, 1000, 1000], dtype=float)

A = np.array([
    [3, 4, 8, 6, -1,   0,   0, 1, 0, 0],
    [2, 2, 7, 5,  0,  -1,   0, 0, 1, 0],
    [6, 4, 7, 4,  0,   0,  -1, 0, 0, 1],
], dtype=float)

b = np.array([
    800,
    200,
    700,
], dtype=float)



M = simplex(matrix=A, rhs=b, z=cj, numxvars=4, direction=-1)


# sols2, z2 = twophase(matrix=A, rhs=b, z=cj, numxvars=4, direction=-1)



