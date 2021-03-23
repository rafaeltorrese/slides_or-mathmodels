"""
Example 04-12

\min Z = 3x_1 2x_2


x_1 + x_2 \geq 1,
x_1 + x_2 \leq 7,
x_1 + 2x_2 \geq 10,
x_2 \leq 3
"""

import numpy as np
import matplotlib.pyplot as plt

from simplex_algorithm import simplex
from twophase_method import twophase
from dualsimplex_algorithm import  dual_simplex
#%%

cj = np.array([-3, -2, 0, 0,  0, 0], dtype=float)

A = np.array([
    [-1, -1, 1, 0, 0, 0],
    [ 1,  1, 0, 1, 0, 0],
    [-1, -2, 0, 0, 1, 0],
    [ 0,  1, 0, 0, 0, 1],
    ], dtype=float)

b = np.array([-1, 7, -10, 3], dtype=float)

#%%
soldualsimplex, gvalues, lastrow = dual_simplex(matrix=A,
                                  rhs=b,
                                  z=cj,
                                  numxvars=2)


#%%

x = np.linspace(0, 100, 100)

eq1 = 1 - x  # x2 >=
eq2 = 7 - x  # x2 <=
eq3 = (10 - x) / 2  # x2 >=
eq4 = 3  # x2 <=

zeq = lambda v,c: (c - 3*v) / 2

#%%

equations_list = [
    (x, eq1),
    (x, eq2),
    (x, eq3),
    ([0, 100], [eq4, eq4])
    ]

equations_label = [
    r'$x_1 + x_2 = 1$',
    r'$x_1 + x_2 = 7$',
    r'$x_1 + 2x_2 = 10$',
    r'$x_2 = 3$',
    ]

#%%
plt.figure(figsize=(8,8))
plt.axvline(0, color="0.4")
plt.axhline(0, color="0.4")

for eq,eqlabel in zip(equations_list, equations_label):
    plt.plot(*eq, lw=3, label=eqlabel)

plt.plot(x, zeq(x, 35), lw=3, ls="--", color="magenta", alpha=0.3, label=r'$\min Z = 3x_1 + 2x_2$')
for z in np.linspace(30, 21, 3):
    plt.plot(x, zeq(x, z), lw=3, ls="--", color="magenta", alpha=0.3)

colors = ("blue", "orange", "green")
deltas = [1, -1, 1]

for eq, color, delta in zip(equations_list[:-1], colors, deltas):
    plt.fill_between(*eq, eq[1] + delta, facecolor=color, alpha=0.3)
plt.axhspan(3, 2, facecolor="red", xmin=0.09, alpha=0.3)



plt.title("Example 04-12")
plt.xlim(-1, 10)
plt.ylim(-1, 10)
plt.legend(fontsize=12, loc="upper right")
plt.show()

#%%
cj = np.array([3, 2, 0, 0,  0, 0, 1000, 1000], dtype=float)

A = np.array([
    [1, 1, -1, 0,  0, 0, 1, 0 ],
    [1, 1,  0, 1,  0, 0, 0, 0],
    [1, 2,  0, 0, -1, 0, 0, 1],
    [0, 1,  0, 0,  0, 1, 0, 0],
    ], dtype=float)

b = np.array([1, 7, 10, 3], dtype=float)
#%%
solsimplex, zvalues = simplex(matrix=A,
                              rhs=b,
                              z=cj,
                              numxvars=2,
                              direction=-1)
#%%
solsimplex, zvalues = twophase(matrix=A,
                              rhs=b,
                              z=cj,
                              numxvars=2,
                              direction=-1)