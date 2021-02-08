"""
max Z = 2x1 + 3x2
subject to
x1 + x2 <= 30
x2 >= 3
x2 <= 12
x1 - x2 >= 0
x1 <= 20

x1, x2 >= 0
"""
import numpy as np
import matplotlib.pyplot as plt

# function domain
x = np.linspace(0, 200, 100)

eq1 = 30 - x   # x2 <= 30 - x1 
eq2 = 3        # x2 >= 3
eq3 = 12       # x2 <= 12
eq4 = x        # x2 <= x1 
eq5 = 20       # x1 <= 20

zeq = lambda x1,z: (z - 2*x1)/3

# ==== Plot =====
plt.figure(figsize=(10,10))
plt.figure('equal')

plt.axvline(0, color="0.4")
plt.axhline(0, color="0.4")

plt.plot(x, eq1, lw=2, label=r"$x_1 + x_2 = 30$")  # eq1
plt.plot([-5, 100], [eq2, eq2], lw=2, label=r"$x_2 = 3$")  # eq2
plt.plot([-5, 100], [eq3,eq3], lw=2, label=f"$x_2 = 12$")  # eq3
plt.plot(x, eq4, lw=2, label=r"$x_1 - x_2 = 0$")  # eq4
plt.plot([eq5, eq5], [-10, 100], lw=2, label=r"$x_1 = 20$")  # eq5

plt.plot(x, zeq(x, 0), color="magenta", lw=3, ls="--", alpha=0.4, label=r"$\max Z = 2x_1 + 3x_2$" )
for i in np.linspace(5, 50, 3):
    plt.plot(x, zeq(x, i), color="magenta", lw=3, ls="--", alpha=0.4)

plt.xlim(-1,35)
plt.ylim(-1, 35)

plt.legend(fontsize=10, loc="upper right")
plt.show()

# ================
# creating matrix and rhs vector
A = np.array([ # Color    Index
    [1,  1],   # blue      [0]
    [0,  1],   # orange    [1]
    [0,  1],   # green     [2] 
    [1, -1],   # red       [3]
    [1,  0],   # purple    [4]
             ])

b = np.array([30, 3, 12, 0, 20])

# intersections
equations_index= [(1, 3),  # orange, red
                  (2, 3),  # green, red
                  (0, 2),  # blue, green
                  (0, 4),  # blue, purple
                  (1, 4),  # orange, purple
                  ]

points = [np.linalg.solve(A[list(i)] , b[list(i)]) for i in equations_index]
coordinates = list(zip(*points))
zvalues = [2*x1 + 3*x2 for x1, x2 in points]
best_index, best_value = max(enumerate(zvalues), key=lambda t:t[1])
best_point = points[best_index]

# ======== Plot =============
plt.figure(figsize=(10,10))
plt.figure('equals')
plt.axvline(0, color='0.4')
plt.axhline(0, color='0.4')

plt.plot(x, eq1, lw=2, label=r"$x_1 + x_2 = 30$")
plt.plot([0, 100], [eq2, eq2], lw=2, label=r"$x_2 = 3$")
plt.plot([0, 100], [eq3, eq3], lw=2, label=r"$x_2 = 12$")
plt.plot(x, eq4, lw=2, label=r"$x_1 - x_2 = 0$")
plt.plot([eq5, eq5], [0, 100], lw=2, label=r"$x_1 = 20$")

plt.plot(x, zeq(x, 0), color="magenta", lw=3, ls="--", alpha=0.4, label=r"$\max Z = 2x_1 + 3x_2$" )
for i in np.linspace(5, 50, 3):
    plt.plot(x, zeq(x, i), lw=3, color="magenta", ls="--", alpha=0.4)

plt.plot(x, zeq(x, best_value), lw=3, color="magenta", ls="--", alpha=0.6)

for point in points:
    plt.plot(*point, ms=7, marker="o", color="k")
plt.plot(*best_point, ms=15, marker="*", color="red")
plt.fill(*coordinates, facecolor="yellow", edgecolor="gray", lw=3, alpha=0.5)

plt.xlim(-1, 35)
plt.ylim(-1, 35)
plt.legend(fontsize=10, loc="upper right")
plt.show()






