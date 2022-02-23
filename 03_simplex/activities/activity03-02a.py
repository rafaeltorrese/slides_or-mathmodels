# %%
from itertools import combinations
import numpy as np
from pprint import pprint
# %%


def labels_combination(variables, nrows):
    return (tuple(combinations(variables, nrows)))


# %%
A = np.array(
    [
        [1, 1, 1, 0, 0, 0, 0],
        [0, 1, 0, -1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0],
        [1, -1, 0, 0, 0, -1, 0],
        [1, 0, 0, 0, 0, 0, 1],
    ]
)

b = np.array(
    [30,
     3,
     12,
     0,
     20, ]
)

z = np.array(
    [
        2,
        3,
        0,
        0,
        0,
        0,
        0,
    ]
)
# %%
labels = np.array('x1 x2 s1 s2 s3 s4 s5'.split())
print(labels)
# %%
m, n = A.shape
comb_list = tuple(combinations(range(n), m))
total_combinations = len(comb_list)
print(f'Number of equations: {m}')
print(f'Number of variables: {n}')
print(f'Number of combinations: {total_combinations}')
# %%
# pprint(comb_list)
comblabels = labels_combination(
    variables=labels, nrows=m)  # combinations with labels
# np.savetxt(fname='./03_simplex/activities/combinations03-02a.csv', X=comblabels,  header='x1 x2 s1 s2 s3 s4 s5', delimiter=',', fmt='%s')
# pprint(np.array(comblabels))

# #%%

# for vars in comb_list:
#     print(labels[[*vars]])
#     print(A[:, [*vars]], '\n')

# %%

vector_solution = np.zeros_like(z)
feasible_solutions = []
feasible_variables = []  # index of columns in matrix A
feasible_labels = []
zvalues = []


infeasible_variables = []  # index of columns in matrix A
infeasbile_solutions = []
infeasbile_labels = []
# %%

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
    # print()


num_infeasibles = len(infeasbile_labels)
print(f'Number of infeasible solutions: {num_infeasibles}')

print()
num_feasible = len(feasible_labels)
print(f'Number of feasibile solutions: {num_feasible}')
print(f'zvalues: {zvalues}')
print('Feasible variables')
idmax, zmax = max(enumerate(zvalues), key=lambda t: t[1])
print(f'The maximum value of z is: {zmax}')
print(
    f'The optimal solution is {feasible_solutions[idmax]}.  \nThe variables are {feasible_labels[idmax]}')
pprint(np.array(feasible_labels).tolist())
