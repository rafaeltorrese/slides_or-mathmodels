'''
\max Z = 3x_1 + 4x_2 
x_1 + x_2 \leq 450,
2x_1 + x_2 \leq 600
x_1, x_2  \geq 0   
'''
from itertools import combinations
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

from analytical_method import  analytical
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

#%%
feasibles, infeasibles, best_solution = analytical(matrix=A, rhs=b, objcoef=cj, constant=0, direction="max")

print(feasibles)
print(infeasibles)

print(best_solution)
print(feasibles[ : , 0:2])
feasible_points = feasibles[:,0:2]
infeasible_points = infeasibles[:,0:2]
print(feasible_points)
print(infeasible_points)

#%%
x = np.linspace(0, 700,100)
eq1 = 450 - x
eq2 = 600 - 2*x

zeq = lambda c,x: (c - 3*x)/4

equations_list = [
    (x, eq1), 
    (x, eq2)]

equations_label = [f"$ x_1 + x_2 = 450 $", 
               f"$ 2x_1  + x_2 = 600$",  
               ]

plt.figure(figsize=(12,10))
plt.axvline(0, color="gray", lw=3)
plt.axhline(0, color="gray", lw=3)

# Equations
for eq, eqlabel in zip(equations_list, equations_label):
    plt.plot(*eq, lw=2, label=eqlabel)

plt.fill_between(x,eq1, eq1 - 700, alpha=0.2)    
plt.fill_between(x,eq2, eq2 - 700, alpha=0.2)

# Objective Function
plt.plot(x, zeq(0, x), color='m', ls="--", alpha=0.5, label=r"$Z =  3x_1 + 4x_2 $")
for i in np.linspace(100, 1600, 6):
    plt.plot(x, zeq(i, x), color='m', ls="--", alpha=0.4)

# ================================
# Feasible
for basic in feasible_points:
    plt.plot(basic[0], basic[1], color='b', marker="o")
# ================================
# Infeasible
for basic in infeasible_points:
    plt.plot(basic[0], basic[1], color="k", marker="o")
# ================================
# Optimal solution
plt.plot(best_solution[0], best_solution[1], color="r", marker="*", ms=12)    # point
plt.plot(x, zeq(best_solution[-1], x), color="#330241", ls="dashed", lw=2, alpha=0.5, 
         label=f"$\max\; Z = {best_solution[-1]} $")  # line
# ================================
plt.legend(loc="upper right", prop={"size":14})
plt.xlim(-50,600)
plt.ylim(-50,650)
plt.show()