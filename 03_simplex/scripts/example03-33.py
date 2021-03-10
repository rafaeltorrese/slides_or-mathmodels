"""
Example 03-33

Max Z = 5x1 + 4x2

6x1 + 4x2 <= 24
x1 + 2x2 <= 6
-x1 + x2 <= 1
x2 <= 2

x1, x2 >= 0
"""

import numpy as np
import matplotlib.pyplot as plt

from analytical_method import analytical
#%%

cj = np.array([5, 4, 0, 0, 0, 0])

A =  np.array([
    [ 6, 4, 1, 0, 0, 0],
    [ 1, 2, 0, 1, 0, 0],
    [-1, 1, 0, 0, 1, 0],
    [ 0, 1, 0, 0, 0, 1],
    ])

b = np.array([24, 6, 1, 2])
#%%
feasibles, infeasibles, best_vector = analytical(matrix=A, rhs=b, objcoef=cj)

print("Total basics: ", feasibles.shape[0] + infeasibles.shape[0])
print("Number of feasibles", feasibles.shape[0])
print("Number of infeasibles", infeasibles.shape[0])
print("Total variables:", feasibles.shape[1] - 1)

points = sorted(feasibles[:, :2], key=lambda t:t[0], reverse=True)
print(points)
best_value = best_vector[-1]
best_point =best_vector[:2]

coordinates = [*zip(*points)]
#%%
x = np.linspace(0, 100, 100)
#%%
eq1 = (24 - 6*x) / 4   # x2 <=
eq2 = ( 6 -   x) / 2   # x2 <=
eq3 =   1 +   x        # x2 <=
eq4 = 2                # x2 <= 2

zeq = lambda v,c: (c - 5*v) / 4

#%%

equations_list = [
    (x, eq1),
    (x, eq2),
    (x, eq3),
    ([0, 100], [eq4, eq4]),
    ]

equations_label = [
    r'$6x_1 + 4x_2 = 24$',
    r'$x_1 + 2x_2 = 6$',
    r'$-x_1 + x_2 = 1$',
    r'$x_2 = 2$',
    ]

#%%
plt.figure(figsize=(10,10))
plt.axvline(0, color="0.4")
plt.axhline(0, color="0.4")

for eq, eqlabel in zip(equations_list, equations_label):
    plt.plot(*eq, lw=3, label=eqlabel)


plt.plot(x, zeq(x, 0), lw=3, ls="--", color="magenta", alpha=0.3, label=r"$\max\, Z = 5x_1 + 4x_2$")
for z in np.linspace(5, 15, 3):
    plt.plot(x, zeq(x, z), lw=3, ls="--", color="magenta", alpha=0.3)
plt.plot(x, zeq(x, best_value), lw=4, ls="--", color="magenta", alpha=0.3, label=fr'$\max\, Z={best_value}$')


for point in infeasibles[:, :2]:
    plt.plot(*point, ls=None, marker="s", ms=6, color="k" )

for point in points:
    plt.plot(*point, ls=None, color="blue", marker="o", ms=6)

plt.plot(*best_point, ls=None, marker="*", ms=12, color="red", label=fr'$x_1:{best_point[0]},\, x_2:{best_point[1]:2.2f}$' )
plt.fill(*coordinates, facecolor="yellow", alpha=0.3)

plt.title("Example 33. Reddy Mikks")
plt.xlim(-0.2,6.5)
plt.ylim(-0.2, 6.5)
plt.legend(fontsize=12, loc="upper right")
plt.show()