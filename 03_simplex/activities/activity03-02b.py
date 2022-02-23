# %%
from itertools import combinations
from pprint import pprint
from tabulate import tabulate

import numpy as np
import pandas as pd

# %%


def labels_combination(variables, nrows):
    return (tuple(combinations(variables, nrows)))


# %%
A = np.array(
    [
        [2, 3, 2, 1, 0, 0],
        [4, 0, 3, 0, 1, 0],
        [2, 5, 0, 0, 0, 1],        
    ]
)

b = np.array(
    [440,
     470,
     430,
    ]
)

z = np.array(
    [
        4,
        3,
        6,
        0,
        0,
        0,        
    ]
)
# %%
labels = np.array('$x_1$ $x_2$ $x_3$ $s_1$ $s_2$ $s_3$'.split())
# %%
m, n = A.shape
comb_list = tuple(combinations(range(n), m))
total_combinations = len(comb_list)

print('-' * 20)
print(f'Number of equations: {m}')
print(f'Number of variables: {n}')
print(f'Number of combinations: {total_combinations}')
# %%
# pprint(comb_list)
comblabels = labels_combination(
    variables=labels, nrows=m)  # combinations with labels
# np.savetxt(fname='./03_simplex/activities/combinations03-02a.csv', X=comblabels,  header='x1 x2 s1 s2 s3 s4 s5', delimiter=',', fmt='%s')
# pprint(np.array(comblabels))

# %%
feasible_solutions = []
feasible_variables = []  # index of columns in matrix A
feasible_labels = []
zvalues = []
#%%
infeasible_variables = []  # index of columns in matrix A
infeasbile_solutions = []
infeasbile_labels = []
# %%
singular_list = []
#%%
print('-' * 20)
for var in comb_list:
    variables = np.array(var)
    # print(labels[variables])
    # print(np.delete(labels, variables))
    try:
        basic_solution = np.linalg.solve(A[:, variables], b)
        if np.any(basic_solution < 0):
            infeasible_variables.append(variables)
            infeasbile_labels.append(labels[variables])
            infeasbile_solutions.append(basic_solution)
            continue
        feasible_variables.append(variables)
        feasible_labels.append(labels[variables])
        feasible_solutions.append(basic_solution)
        zvalue = z[variables].dot(basic_solution)
        zvalues.append(zvalue)
    except np.linalg.LinAlgError as LA:        
        print(f'{LA} with system {labels[variables]}')
        singular_list.append(labels[variables])


num_infeasibles = len(infeasbile_labels)
num_feasible = len(feasible_labels)
num_singular = len(singular_list)

print('-' * 20)
print(f'Number of feasibile solutions: {num_feasible}')
print(f'Number of infeasible solutions: {num_infeasibles}')
print(f'Number of singular systems: {num_singular}')
print('-' * 20)

idopt, zopt = max(enumerate(zvalues), key=lambda t: t[1])
print(f'The maximum value of z is: {zopt} at index {idopt}')

print(
    f'The optimal solution is {feasible_solutions[idopt]}.  \nThe variables are {feasible_labels[idopt]}')

print('-' * 20)
print('Feasible variables')
print(
    tabulate(
        np.array(feasible_labels).tolist(),
        tablefmt='latex'
    )    
    )




print('-' * 20)
print('Singular matrix with the following variables:')
print(
    tabulate(
        singular_list,
        tablefmt='latex'
    )
)
