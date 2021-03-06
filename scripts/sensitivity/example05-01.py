"""
maximize Z = 5x1 + 12x2 + 4x3,
subject to 

x1 + 2x2 + x3  <= 5,
2x1 - x2 + 3x3  = 2
"""
import os
os.chdir("..")

import numpy as np
np.set_printoptions(precision=3, suppress=True)

#%%
from auxfunc.dualsimplex_algorithm import dual_simplex
from auxfunc.algorithms import simplex
from auxfunc.algorithms import create_fullmatrix
#%%


cj = [5, 12, 4]

A = [
     [1, 2, 1],
     [2, -1, 3],
     ]

b = [5, 2]

ineq = ["<=", "="]

primal_solutions, zvalues, lastrow_primal, optitable_primal = simplex(matrix=A,
                                                                      rhs=b,
                                                                      z=cj,
                                                                      inequalities=ineq,
                                                                      direction=1)

