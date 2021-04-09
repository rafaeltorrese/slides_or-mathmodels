"""
maximize Z = -x1 + 2x2 - x3,
subject to 

3x1 + x2 - x3  <= 10
-x1 + 4x2 + x3  >= 6
x2 + x3 <= 4
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


cj = [-1, 2, -3]

A = np.array([
     [ 3,  1,-1],
     [-1,  4, 1],
     [ 0,  1, 1],
     ], dtype=float)

b = [10, 6, 4]

ineq = ["<=", ">=", "<="]

primal_solutions, zvalues, lastrow_primal, optitable_primal = simplex(matrix=A,
                                                                      rhs=b,
                                                                      z=cj,
                                                                      inequalities=ineq,
                                                                      direction=1)


Afull, labels, cjfull = create_fullmatrix(body=A, 
                                          inequalities=ineq,
                                          c=cj)


B = Afull[:, [1, 3, 4]]

Binv = np.linalg.inv(B)
