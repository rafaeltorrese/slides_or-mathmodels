'''
\max Z = 3x_1 + 4x_2 
x_1 + x_2 \leq 450,
2x_1 + x_2 \leq 600
x_1, x_2  \geq 0   
'''
from itertools import combinations
import numpy as np

#%%
cj = np.array([
    3,  # x1
    4,  # x2
    0,  # s1
    0,  # s2
])

# standard form
A = np.array([
    # x1 x2 s1 s2
    [1, 1, 1, 0],
    [2, 1, 0, 1],
])

b = np.array([
    450,
    600,
])



m, n = A.shape  # num_rows and num_cols
variables = [*combinations(range(n), m)]  # n variables taken m at a time without repetition
print(variables)
print(variables[0])
print(variables[1])
#%%
print("Total combinations", len(variables))
#%%
solution1 = np.zeros_like(cj)
solution2 = np.zeros_like(cj)
solution3 = np.zeros_like(cj)
solution4 = np.zeros_like(cj)
solution5 = np.zeros_like(cj)
solution6 = np.zeros_like(cj)


#%%
for var in variables:
    print(A[:, [*var]], "\n")

#%%
print(f"Variables {variables[0]}") # Point 1
print(f"Subsystem \n {A[:, variables[0]]}")
print(f"Right-hand side: \n {b}")
basic1 = np.linalg.solve(A[:, variables[0]], b)
print(f"Basic1 for variables {variables[0]} \n {basic1}")
print("is feasible?", np.all(basic1 <= b) and np.all(basic1 >= 0))
solution1[[*variables[0]]] = basic1
print("Solution1", solution1)
print("z1", cj[[*variables[0]]].dot(basic1))

#%%
print() # Point 2
print(f"Variables {variables[1]}")
print(f"Subsystem \n {A[:, variables[1]]}")
print(f"Right-hand side: \n {b}")
basic2 = np.linalg.solve(A[:, variables[1]], b)
print(f"Basic2 for variables {variables[1]} \n {basic2}")
print("is feasible?", np.all(basic2 <= b) and np.all(basic2 >= 0) )
solution2[[*variables[1]]] = basic2
print("Solution2", solution2)

#%%
print() # Point 3
print(f"Variables {variables[2]}")
print(f"Subsystem \n {A[:, variables[2]]}")
print(f"Right-hand side: \n {b}")
basic3 = np.linalg.solve(A[:, variables[2]], b)
print(f"Basic3 for variables {variables[2]} \n {basic3}")
print("is feasible?", np.all(basic3 <= b) and np.all(basic3 >= 0) )
solution3[[*variables[2]]] = basic3
print("Solution3", solution3)

#%%
print()  # Point 4
print(f"Variables {variables[3]}")
print(f"Subsystem \n {A[:, variables[3]]}")
print(f"Right-hand side: \n {b}")
basic4 = np.linalg.solve(A[:, variables[3]], b)
print(f"Basic4 for variables {variables[3]} \n {basic4}")
print("is feasible?", np.all(basic4 <= b) and np.all(basic4 >= 0) )
solution4[[*variables[3]]] = basic4
print("Solution4", solution4)
#%%
print()  # Point 5
print(f"Variables {variables[4]}")
print(f"Subsystem \n {A[:, variables[4]]}")
print(f"Right-hand side: \n {b}")
basic5 = np.linalg.solve(A[:, variables[4]], b)
print(f"Basic5 for variables {variables[4]} \n {basic5}")
print("is feasible?", np.all(basic5 <= b) and np.all(basic5 >= 0) )
solution5[[*variables[4]]] = basic5
print("Solution5", solution5)

#%%
print()  # Point 6
print(f"Variables {variables[5]}")
print(f"Subsystem \n {A[:, variables[5]]}")
print(f"Right-hand side: \n {b}")
basic6 = np.linalg.solve(A[:, variables[5]], b)
print(f"Basic6 for variables {variables[5]} \n {basic6}")
print("is feasible?", np.all(basic6 <= b) and np.all(basic6 >= 0) )
solution6[[*variables[5]]] = basic6
print("Solution6", solution6)
