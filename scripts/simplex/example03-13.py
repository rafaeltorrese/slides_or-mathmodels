# -*- coding: utf-8 -*-
"""
Example 13 Slides
Example 02.10-04 Gupta ebook
max Z = -4x1 + 3x2

subject to

x_1 - x_2 \leq 0
x_1  \leq 4

"""

import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# domain function
x = np.linspace(0, 50, 50)

# constraints
eq1 = x   # x2 >=
eq2 = 4   # x1 <=

# z equation
zeq = lambda v, c: (c  + 4*v) / 3   #  x2 = (Z  + 4x1) / 3

# equations
equations_list = [(x, eq1),
                  ([eq2, eq2], [-5, 50] ),
                  ]  

# labels
equations_label = [r"$x_1 - x_2 = 0$",
                   r"$x_1 = 4$",
                   ]

# Plot
plt.figure(1, figsize=(7,7))
plt.axvline(0, color="0.4")
plt.axhline(0, color="0.4")

# plo equations
for eq, eqlabel in zip(equations_list, equations_label):
    plt.plot(*eq, lw=2, label=eqlabel)
# plot z function
plt.plot(x, zeq(x, 0), lw=3, ls="--", color="magenta", alpha=0.3, label="$\max\; Z = -4x_1 + 3x_2$")
for z in np.linspace(6,24, 3):
    plt.plot(x, zeq(x, z), lw=3, ls="--", color="magenta", alpha=0.3)
# areas
plt.fill_between(x, eq1, eq1 + 5, facecolor="blue", alpha=0.3)
plt.axvspan(2, eq2, facecolor="orange", alpha=0.3)
# plt.fill_between(x, eq1, 100, where=x<=4, color="0.7", interpolate=True)
#
plt.xlim(-0.5, 10)
plt.ylim(-0.5, 10)
# plt.axis([-0.5, 10, -0.5, 10])
plt.title("Unbounded Solution")
plt.legend(fontsize=15, loc="upper right")
plt.show()