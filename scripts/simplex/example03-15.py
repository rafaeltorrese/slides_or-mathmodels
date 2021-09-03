"""
\max Z = 3x_1 + 2x_2
subject to
-2x_1 + 3x_2 \leq 9,
3x_1 - 2x_2  \leq -20
x_1, x_2 \geq 0
"""
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# function domain
x = np.linspace(-10, 60, 60)

# equations
eq1 = ( 9   + 2*x ) / 3   # x2 <=
eq2 = ( 3*x +  20 ) / 2   # x2 >= 

# z equation
zeq = lambda v, c: (c - 3*v) / 2

# equations
equations_list = [(x, eq1),
                  (x, eq2),
                  ]
# labels
equations_label = [r"$-2x_1 + 3x_2 \leq 9,$",
                   r"$3x_1 - 2x_2  \leq -20$",
                   ]

plt.figure(1, figsize=(7,7))
plt.axis("equal")

plt.axvline(0, color="0.4")
plt.axhline(0, color="0.4")

# plot equations
for eq, eqlabel in zip(equations_list,equations_label):
    plt.plot(*eq, lw=2, label=eqlabel)
# plot z function
plt.plot(x, zeq(x, 0), lw=3, ls="--", color="magenta", alpha=0.3, label=r"$\max\; Z = 3x_1 + 2x_2$" )
for z in np.linspace(20, 100, 4):
    plt.plot(x, zeq(x, z), lw=3, ls="--", color="magenta", alpha=0.3)
#
plt.fill_between(x, eq1, eq1 - 20, facecolor="blue", alpha=0.4)
plt.fill_between(x, eq2, eq2 + 20, facecolor="orange", alpha=0.4)
#
plt.xlim(-2, 20)
plt.ylim(-2, 20)
plt.legend(fontsize=15, loc="upper right")
plt.title("Infeasible Solution")
plt.show()
