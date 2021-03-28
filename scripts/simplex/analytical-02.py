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

x = np.linspace(0, 700,100)
eq1 = 450 - x
eq2 = 600 - 2*x

zeq = lambda c,x: (c - 3*x)/4

equations_list = [
    (x, eq1),
    (x, eq2)]

equations_label = [
    r"$ x_1 + x_2 = 450 $",
    r"$ 2x_1  + x_2 = 600$",
               ]

plt.figure(figsize=(10,10))
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
plt.legend(loc="upper right", fontsize=15)
plt.xlim(-50,650)
plt.ylim(-50,650)
plt.show()
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
feasibles, infeasibles, best_solution = analytical(matrix=A, rhs=b, objcoef=cj)
feasible_points = feasibles[:,0:2]

print(feasible_points)
sorted_points = sorted(feasible_points, key=lambda t:t[1], reverse=True)
infeasible_points = infeasibles[:,0:2]
coordinates = [*zip(*sorted_points)]
print(coordinates)
#%%
x = np.linspace(0, 700,100)
eq1 = 450 - x
eq2 = 600 - 2*x

zeq = lambda c,x: (c - 3*x)/4

equations_list = [
    (x, eq1),
    (x, eq2)]

equations_label = [
    r"$ x_1 + x_2 = 450 $",
    r"$ 2x_1  + x_2 = 600$",
               ]

plt.figure(figsize=(10,10))
plt.axvline(0, color="gray", lw=3)
plt.axhline(0, color="gray", lw=3)

# Equations
for eq, eqlabel in zip(equations_list, equations_label):
    plt.plot(*eq, lw=2, label=eqlabel)

# plt.fill_between(x, np.minimum(eq1, eq2), where=(x < 300), facecolor="0.8")
plt.fill(*coordinates, color="0.7")

# Objective Function
plt.plot(x, zeq(0, x), color='m', ls="--", alpha=0.5, label=r"$Z =  3x_1 + 4x_2 $")
for i in np.linspace(100, 1600, 6):
    plt.plot(x, zeq(i, x), color='m', ls="--", alpha=0.4)

# ================================
# Feasible
for basic in feasible_points:
    plt.plot(*basic, color='b', marker="o", ms=10)
# ================================
# Infeasible
for basic in infeasible_points:
    plt.plot(basic[0], basic[1], color="k", marker="o", ms=10)
# ================================
# Optimal solution
plt.plot(*best_solution[:2], color="r", marker="*", ms=18)    # point
plt.plot(x, zeq(best_solution[-1], x), color="#330241", ls="dashed", lw=2, alpha=0.5,
         label=f"$\max\; Z = {best_solution[-1]} $")  # line
# ================================
plt.legend(loc="upper right", fontsize=15)
plt.xlim(-50,650)
plt.ylim(-50,650)
plt.show()