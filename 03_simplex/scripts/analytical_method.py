"""
Analytical Method
"""
from itertools import combinations
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

#%%
def analytical(matrix, rhs, objcoef, constant=0, direction="max"):
    num_rows, num_cols = matrix.shape
    lst_feasible = []    # list of feasible solutions
    lst_infeasible = []
    for variables in combinations(range(num_cols), num_rows):
        try:
            vector = np.zeros(num_cols)   # zero vector  [0, 0, 0, ... , 0]
            basic = np.linalg.solve(matrix[:, variables], rhs)
            vector[list(variables)] = basic
            z = objcoef.dot(vector) + constant
            solution = np.concatenate([vector, [z]])   # [x1, x2, x,3] + [zvalue] = [x1, x2, x3, zvalue]
            if np.any(basic < 0):   # infeasible
                lst_infeasible.append(solution)
            else:
                lst_feasible.append(solution)  # feasible solutions
        except np.linalg.LinAlgError:
            print(f"Singular Matrix with variables {variables}")
    feasible_solutions = np.array(lst_feasible)
    infeasible_solutions = np.array(lst_infeasible)  # array of infeasble solutions
    if direction == "max":
        best_solution = np.argmax(feasible_solutions[:, -1])  # last column with z value
    else:
        best_solution = np.argmin(feasible_solutions[:, -1])
    best_vector = feasible_solutions[best_solution]
    return feasible_solutions, infeasible_solutions,  best_vector