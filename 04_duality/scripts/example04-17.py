"""
\min Z = 2x_1 + x_2

3x_1 + x_2 \geq 3
4x_1 + 3x_2 \geq 6
x_1+ 2x_2 \geq 3
"""
import re
import numpy as np
from algorithms import simplex, twophase, dual_simplex

c = np.array([2, 1], dtype=float)

body = np.array([
    [3, 1],
    [4, 3],
    [1, 2],
    ] , dtype=float)

b = np.array([3,6,3], dtype=float)

sense = "min"

inequalities = [">=", ">=", ">="]


if sense == "min":
    cds = -1 * np.array(c)  # cds, c dual simplex
    for i, ineq in enumerate(inequalities):
        if ineq == ">=":
            row = body[i]
            bi = b[i]
            body[i] = -1 * row
            b[i] = -b[i]



print(cds)
print(body)
print(b)

