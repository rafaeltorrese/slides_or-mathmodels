"""
\min Z = 2x_1 + x_2

3x_1 + x_2 \geq 3
4x_1 + 3x_2 \geq 6
x_1+ 2x_2 \geq 3
"""
import os
os.chdir('..')
import numpy as np
np.set_printoptions(precision=3, suppress=True)
#%%
from auxfunc.dualsimplex_algorithm import dual_simplex
from auxfunc.algorithms import simplex as simplex2
from auxfunc.algorithms import create_fullmatrix
#%%


cj = np.array([-2, -1, 0, 0, 0], dtype=float)

A = np.array([
    [-3, -1, 1, 0, 0],
    [-4, -3, 0, 1, 0],
    [-1, -2, 0, 0, 1],
    ] , dtype=float)

b = np.array([-3, -6, -3], dtype=float)


#%%
soldualsimplex, gvalues, lastrow = dual_simplex(matrix=A,
                                  rhs=b,
                                  z=cj,)

#%%
cjprimal = -1 * cj[:2]

Aprimal = -1 * A[:,:2]
ineqprimal = [">=", ">=", ">="]

bprimal = -1 * b[:]


#%%
cjdual = bprimal[:]
bdual = cjprimal[:]
ineqdual = ["<=", "<="]
Adual = np.array(Aprimal).T

#%%
print()
solutions, zvalues, lastrows = simplex2(matrix=Aprimal, rhs=bprimal, z=cjprimal, inequalities=ineqprimal, direction=-1)

print()

solutions, zvalues, lastrows = simplex2(matrix=Adual, rhs=bdual, z=cjdual, inequalities=ineqdual, direction=1, vlabel="y")