#%%
from itertools import combinations
import numpy as np

#%%
z = np.array([1, 3, 3])

A = np.array([
    [1, 2, 3],
    [2, 3, 5],
])

b = np.array([
    4,
    7,
])
#%%
num_constraints, num_variables = A.shape

columns_index = [*combinations(range(num_variables), num_constraints )]
num_matrix = len(columns_index)
print(num_matrix)

# print(A[: , columns_index[0]]) 
#%%
sys_eq01 = A[: , columns_index[0]]
sys_eq02 = A[: , columns_index[1]]
sys_eq03 = A[: , columns_index[2]]
#%%
solution1 = np.zeros_like(z)
solution2 = np.zeros_like(z)
solution3 = np.zeros_like(z)
#%%
print(A)
print()
print(sys_eq01, '\n')
print(sys_eq02, '\n')
print(sys_eq03)
#%%
solution1[list(columns_index[0])] = np.linalg.solve(sys_eq01, b)
solution2[list(columns_index[1])] = np.linalg.solve(sys_eq02, b)
solution3[list(columns_index[2])] = np.linalg.solve(sys_eq03, b)
#%%
print(solution1)
print(solution2)
print(solution3)
#%%
print(solution1 >= 0)
print(solution2 >= 0)
print(solution3 >= 0)  # infeasible
#%%
if (solution1 >= 0).any():
    print(f"Solution {solution1} is feasible")
else:
    print(f"Solution {solution1} is infeasible")

if (solution2 >= 0).any():
    print(f"Solution {solution2} is feasible")
else:
    print(f"Solution {solution2} is infeasible")

if (solution3 >= 0).any():
    print(f"Solution {solution3} is feasible")
else:
    print(f"Solution {solution3} is infeasible")

#%%
z1 = z.dot(solution1)
z2 = z.dot(solution2)
z3 = z.dot(solution3)

print(z1)
print(z2)
print(z3)

#%%
solutions = [solution1, solution2]
# only feasible solutions
zvalues = [z1, z2]

print()
print(zvalues)
print(max(zvalues))
#%%
best_index, best = max(enumerate(zvalues), key=lambda t:t[1])
print(best_index, best)
#%%
best_solution = solutions[best_index]
print(best_solution)
print(f'Optimal solution found at {best_solution} with zvalue: {best}')