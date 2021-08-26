"""
max Z = 2x1 + x2

x1 + 2x2 <= 10
x1 + x2 <= 6
x1 - x2 <= 2
x1 - 2x2 <= 1

x1, x2 >= 0
"""

import numpy as np
import  matplotlib.pyplot as plt



# function domain
x = np.linspace(0,100, 50)
# ==== constraints =====
eq1 = (10 - x)/2   # x2 = (10 - x1)/10
eq2 = 6 - x        # x2 = 6 - x1
eq3 = x - 2        # x2 = x1 - 2
eq4 = (x - 1)/2    # x2 = (x1 - 1)/2
# =======zfunction===========
zeq = lambda x1, z: z - 2*x1   # x2 = Z - 2x1
equations_list = [(x, eq1),
                  (x, eq2),
                  (x, eq3),
                  (x, eq4)]

equation_labels = [r"$x_1 + 2x_2 \leq 10$",  # blue
                   r"$x_1 + x_2 \leq 6$",    # orange
                   r"$x_1 - x_2 \leq 2$",    # green
                   r"$x_1 - 2x_2 \leq 1$",   # red
                   ]

plt.figure(figsize=(8,8))
plt.axvline(0, color="0.4")
plt.axhline(0, color="0.4")
for equation, eqlabel in zip(equations_list, equation_labels):
    plt.plot(*equation, lw=2, label=eqlabel)

plt.plot(x, zeq(x, 0), color="magenta", lw=3, ls="--", label=r"$\max\, Z = 2x_1 + x_2$", alpha=0.4)
for i in np.linspace(2, 6, 3):
    plt.plot(x, zeq(x, i), color="magenta", lw=3, ls="--", alpha=0.4)
plt.xlim(-1, 8)
plt.ylim(-1, 8)
plt.legend(fontsize=10, loc="upper right")
plt.show()

# coefficient matrix (left-hand side)
A = np.array([ # Color   Index
    [1,  2],   # blue    0
    [1,  1],   # orange  1
    [1, -1],   # green   2
    [1, -2],   # red     3
    [0,  1],   # gray    4 x Axis
    [1,  0],   # gray    5 y Axis
    ])

# column-vector
b = np.array([10,
              6,
              2,
              1,
              0, # x Axis
              0, # y Axis
              ])

# Only lines with intersecting each other
equations_index = [(4, 5),  # xAxis, yAxis 
                   (4, 3),  # xAxis, red
                   (2, 3),  # green, red
                   (1, 2),  # orange, green
                   (0, 1),  # blue, orange
                   (0, 5),  # blue, yAxis
                   ]

points = [np.linalg.solve(A[list(i)], b[list(i)]) for i in equations_index]
# print([*enumerate(2*x1 + x2 for x1, x2 in points)])
best_index, best_value = max(enumerate(2*x1 + x2 for x1, x2 in points), key=lambda t:t[1])
best_point = points[best_index]

coordinates = [*zip(*points)]

plt.figure(figsize=(8,8))
# plt.figure("equals")
plt.axvline(0, color="0.4")
plt.axhline(0, color="0.4")

for eq,eqlabel in zip(equations_list, equation_labels):
    plt.plot(*eq, lw=2, label=eqlabel)

plt.plot(x, zeq(x, 0), color="magenta", lw=3, ls="--", alpha=0.4, label=r"$\max\, Z = 2x_1 + x_2$")
for i in np.linspace(2, 6, 3):  # zvalue lines
    plt.plot(x, zeq(x, i), color="magenta", lw=3, ls="--", alpha=0.4)
plt.plot(x, zeq(x, best_value), color="magenta", lw=3, ls="--", alpha=0.6)  # optimal solution line

for point in points:
    plt.plot(*point, color="k", marker="o", ms=7)
plt.plot(*best_point, color="red", marker="*", ms=14)

plt.fill(*coordinates, facecolor="yellow", edgecolor="gray", lw=4, alpha=0.4)

plt.xlim(-1, 8)
plt.ylim(-1, 8)
plt.legend(fontsize=10, loc="upper right")
plt.show()
  

