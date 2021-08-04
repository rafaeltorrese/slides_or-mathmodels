"""
Example 03-32
Example 04-08

Max Z = 2x1 + x2

x1 + 2x2  <= 10
x1 + x2 <= 6
x1 - x2 <= 2
x1 - 2x2 <= 1
"""
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=3, suppress=True)
#%%
from  analytical_method import analytical
from simplex_algorithm import simplex
from twophase_method import twophase
#%%

x = np.linspace(0, 100, 100)

eq1 = (10 - x) / 2  # <=
eq2 = 6 - x         # <=
eq3 = x - 2          # >=
eq4 = (x - 1) / 2  # >=

zeq = lambda v,c: (c - 2*v)

equations_list = [
    (x, eq1),
    (x, eq2),
    (x, eq3),
    (x, eq4),
    ]

equations_label = [
    r"$x_1 + 2x_2 = 10$",
    r"$x_1 + x_2 = 6$",
    r"$x_1 - x_2 = 2$",
    r"$x_1 - 2x_2 = 1$",
    ]

#%%

cj = np.array([2, 1, 0, 0, 0, 0], dtype=float)

A = np.array([
    [1,  2, 1, 0, 0, 0],
    [1,  1, 0, 1, 0, 0],
    [1, -1, 0, 0, 1, 0],
    [1, -2, 0, 0, 0, 1],
    ], dtype=float)

b = np.array([10, 6, 2, 1], dtype=float)

feasibles, infeasibles, best_vector = analytical(matrix=A, rhs=b, objcoef=cj)
feasibles_points = sorted(feasibles[:, :2], key=lambda t:t[1], reverse=True)
coordinates = [*zip(*feasibles_points)]

#%%


solsimplex, zvalues = simplex(matrix=A, rhs=b, z=cj, numxvars=2)



#%%


# dual Min

print("Dual Problem\n")
c2j = np.array([10, 6, 2, 1, 0, 0, 1000, 1000], dtype=float)

A2 = np.array([
    [1, 1,  1,  1, -1,  0, 1, 0],
    [2, 1, -1, -2,  0, -1, 0, 1],
    ], dtype=float)

b2 = np.array([2, 1], dtype=float)


#%%
soldual, wvalues = simplex(matrix=A2, rhs=b2, z=c2j, numxvars=4, direction=-1)

#%%
plt.figure(figsize=(8,8))
plt.axvline(0, color="0.4")
plt.axhline(0, color="0.4")

for eq, eqlabel in zip(equations_list, equations_label):
    plt.plot(*eq, lw=2, label=eqlabel)

plt.plot(x, zeq(x, 0), lw=3, ls="--", color="magenta", alpha=0.3, label=r"$ \max\, Z = 2x_1 + x_2$")
for z in zvalues[:-1]:
    plt.plot(x, zeq(x, z), lw=3, ls="--", color="magenta", alpha=0.3)


for w in wvalues[:-1]:
    plt.plot(x, zeq(x, w), lw=3, ls="--", color="brown", alpha=0.3)

for point in feasibles_points:
    plt.plot(*point, color="blue", marker="o", ms=5)

plt.plot(*solsimplex[-1], color="red", marker="*", ms=15, ls="", label=r'')

plt.fill(*coordinates, facecolor="yellow", alpha=0.3)


plt.xlim(-1, 11)
plt.ylim(-1, 11)
plt.legend(fontsize=12, loc="upper right")
plt.show()
#%%
print(solsimplex[-1])
print()
print(soldual[-1])
#%%

print()
print(A[:, :2].dot(solsimplex[-1, :2]))
print(b)
#%%
print()
print(A2[:, :4].dot(soldual[-1, :4] ))
print(b2)
