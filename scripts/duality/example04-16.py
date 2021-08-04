"""
Example 04-16
\min Z = 3x_1 + 2x_2 + x_3 + 4x_4
2x_1 + 4x_2 + 5x_3 + x_4 \geq 10
3x_1 - x_2 + 7x_3 - 2x_4 \geq 2
5x_1 + 2x_2 + x_3 +6x_4 \geq 15
"""
import os
import numpy as np
np.set_printoptions(precision=3, suppress=True)
#%%
from auxfunc.dualsimplex_algorithm import dual_simplex
from auxfunc.algorithms import simplex as simplex2
from auxfunc.algorithms import create_fullmatrix
#%%
os.chdir('..')
#%%
cj = np.array([-3, -2, -1, -4] , dtype=float)

A = np.array([
    [-2, -4, -5, -1],
    [-3,  1, -7,  2],
    [-5, -2, -1, -6],
    ] , dtype=float)

b = np.array([-10, -2, -15] , dtype=float)

ineq = ["<="] * 3
#%%
soldualsimplex, gvalues, lastrow = dual_simplex(matrix=A,
                                                inequalities=ineq,
                                                rhs=b,
                                                z=cj,
                                                )

#%%
cjprimal = [3, 2, 1, 4]

Aprimal = [
    [2,  4, 5,  1],
    [3, -1, 7,  2],
    [5,  2, 1,  6],
    ]
ineqprimal = [">=", ">=", ">="]

bprimal = [10, 2, 15]


#%%
cjdual = bprimal[:]
bdual = cjprimal[:]
ineqdual = ["<=", "<=", "<=", "<="]
Adual = np.array(Aprimal).T

#%%
# print()
solutions, zvalues, lastrows, optitable_primal = simplex2(matrix=Aprimal, rhs=bprimal, z=cjprimal, inequalities=ineqprimal, direction=-1)

# print()

solutions, zvalues, lastrows, optitable_dual = simplex2(matrix=Adual, rhs=bdual, z=cjdual, inequalities=ineqdual, direction=1, vlabel="y")