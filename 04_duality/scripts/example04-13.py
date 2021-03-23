"""
\max Z = 2x_1 + 3x_2
x_1 + x_2  \leq 30
x_2  \geq 3
x_2  \leq 12
x_1 - x_2  \geq 0
x_1   \leq 20
x_1, x_2 & \geq 0
"""

import numpy as np
np.set_printoptions(precision=3, suppress=True)

import matplotlib.pyplot as plt

#%%
from simplex_algorithm import simplex
from dualsimplex_algorithm import dual_simplex
#%%
x = np.linspace(0, 100, 100)

eq1 = 30 - x  # x2 <=
eq2 = 3       # x2 >=
eq3 = 12      # x2 <=
eq4 = x       # x2 <=
eq5 = 20      # x1 <=

zeq = lambda v, c: (c - 2*v) / 3
#%%
equations_list = [
    (x, eq1),
    ([0, 100], [eq2, eq2]),
    ([0, 100], [eq3, eq3]),
    (x, eq4),
    ([eq5, eq5], [0, 100]),
    ]

equations_label = [
    r'$x_1 + x_2 = 30$',
    r'$x_2 = 3$',
    r'$x_2 = 12$',
    r'$x_1 - x_2 = 0$',
    r'$x_1  = 20$',
    r'$x_1, x_2 = 0$',
    ]
#%%
cj = np.array([2,3,0,0,0,0,0], dtype=float)

A = np.array([
    [1,  1, 1,  0, 0,  0, 0],
    [0,  1, 0, -1, 0,  0, 0],
    [0,  1, 0,  0, 1,  0, 0],
    [1, -1, 0,  0, 0, -1, 0],
    [1,  0, 0,  0, 0,  0, 1],
    ]
    , dtype=float)

b = np.array([30, 3, 12, 0, 20], dtype=float)


#%% Simplex Methdo

cj = np.array([2,3,0,0,0,0,0,-1000,-1000], dtype=float)

A = np.array([
    [1,  1, 1,  0, 0,  0, 0,  0, 0],
    [0,  1, 0, -1, 0,  0, 0,  1, 0],
    [0,  1, 0,  0, 1,  0, 0,  0, 0],
    [1, -1, 0,  0, 0, -1, 0,  0, 1],
    [1,  0, 0,  0, 0,  0, 1,  0, 0],
    ]
    , dtype=float)
points,zs = simplex(matrix=A, rhs=b, z=cj, numxvars=2)



#%%
plt.figure(figsize=(8,8))
plt.axvline(0, color='0.4')
plt.axhline(0, color='0.4')

for eq, eqlabel in zip(equations_list, equations_label):
    plt.plot(*eq, lw=2, label=eqlabel)

plt.plot(x, zeq(x, 0), lw=3, ls="--", color="magenta", alpha=0.4, label=r'$\max\, z = 2x_1 + 3x_2 $')
for z in np.linspace(10,50, 5):
    plt.plot(x, zeq(x, z), lw=3, ls="--", color='magenta', alpha=0.4 )

for z in zs:
    plt.plot(x, zeq(x, z), lw=4, ls="--", color='cyan', alpha=0.4 )

for point in points[:, :2]:
    plt.plot(*point, marker="o", color="blue", ls="", ms=7)



plt.xlim(-1,35)
plt.ylim(-1, 35)
plt.legend(fontsize=13, loc="upper right")
plt.show()

#%% Dual Simplex Method

print("Dual Simplex Method")

cj = np.array([2,3,0,0,0,0,0], dtype=float)

A = np.array([
    [ 1,  1, 1,  0, 0,  0,  0],
    [ 0, -1, 0,  1, 0,  0,  0],
    [ 0,  1, 0,  0, 1,  0,  0],
    [-1,  1, 0,  0, 0,  1,  0],
    [ 1,  0, 0,  0, 0,  0,  1],
    ]
    , dtype=float)


b = np.array([30, -3, 12, 0, 20], dtype=float)

soldualsimplex, gvalues, lastrow = dual_simplex(matrix=A,
                                  rhs=b,
                                  z=cj,
                                  numxvars=2)

