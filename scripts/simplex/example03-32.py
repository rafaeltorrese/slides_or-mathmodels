"""
Example 03-32

Max Z = 2x1 + x2

x1 + 2x2  <= 10
x1 + x2 <= 6
x1 - x2 <= 2
x1 - 2x2 <= 1
"""
import numpy as np
import matplotlib.pyplot as plt

from  analytical_method import analytical

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



plt.figure(figsize=(8,8))
plt.axvline(0, color="0.4")
plt.axhline(0, color="0.4")

for eq, eqlabel in zip(equations_list, equations_label):
    plt.plot(*eq, lw=2, label=eqlabel)

plt.plot(x, zeq(x, 0), lw=3, ls="--", color="magenta", alpha=0.3, label=r"$ \max\, Z = 2x_1 + x_2$")
for z in np.linspace(2, 8, 4):
    plt.plot(x, zeq(x, z), lw=3, ls="--", color="magenta", alpha=0.3)

plt.fill_between(x, eq1, eq1 - 5, color="blue", alpha=0.3, interpolate=True)
plt.fill_between(x, eq2, eq2 - 5, color="orange", alpha=0.3, interpolate=True)
plt.fill_between(x, eq3, eq3 + 5, color="green", alpha=0.3, interpolate=True)
plt.fill_between(x, eq4, eq4 + 5, color="red", alpha=0.3, interpolate=True)

plt.xlim(-1, 11)
plt.ylim(-1, 11)
plt.legend(fontsize=12, loc="upper right")
plt.show()


# ================================================
cj = np.array([2, 1, 0, 0, 0, 0])

A = np.array([
    [1,  2, 1, 0, 0, 0],
    [1,  1, 0, 1, 0, 0],
    [1, -1, 0, 0, 1, 0],
    [1, -2, 0, 0, 0, 1],
    ])
b = np.array([10, 6, 2, 1])
# ================================================
feasibles, infeasibles, best_vector = analytical(matrix=A, rhs=b, objcoef=cj)
# points = feasibles[:, :2]
points = sorted(feasibles[:, :2], key=lambda t:t[1], reverse=True)
best_point = best_vector[:2]
best_value = best_vector[-1]


coordinates = [*zip(*points)]

# ================================================
plt.figure(figsize=(8,8))
plt.axvline(0, color="0.4")
plt.axhline(0, color="0.4")

for eq, eqlabel in zip(equations_list, equations_label):
    plt.plot(*eq, lw=2, label=eqlabel)

plt.plot(x, zeq(x, 0), lw=3, ls="--", color="magenta", alpha=0.3, label=r"$ \max\, Z = 2x_1 + x_2$")
for z in np.linspace(2, 8, 4):
    plt.plot(x, zeq(x, z), lw=3, ls="--", color="magenta", alpha=0.3)

plt.plot(x, zeq(x, best_value), ls="--", lw=4, color="magenta", alpha=0.4, label=fr"$\max\, Z = {best_value}$")

for point in points:
    plt.plot(*point, color="blue", marker="o", ms=5)

plt.plot(*best_point, marker="*", ms=10, ls="", color="red", label=fr"$x_1:{best_point[0]},\, x_2:{best_point[1]}$")

# plt.fill_between(x, np.minimum(eq1, eq2), np.maximum.reduce([eq3, eq4, np.zeros_like(x)]), where=(x<4), facecolor="gray",alpha=0.5, interpolate=True)

plt.annotate("Iter1", xy=(1,0), xytext=(0.5, 0.3) )
plt.annotate("Iter2", xy=(3,1), xytext=(2.5, 1.3) )
plt.annotate("Iter3", xy=(4,2), xytext=(3.5, 2.3) )

plt.fill(*coordinates, facecolor="yellow", alpha=0.3)


plt.xlim(-1, 11)
plt.ylim(-1, 11)
plt.legend(fontsize=12, loc="upper right")
plt.show()