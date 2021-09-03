"""
Example 12
Example 02.10-03 GuptaEbook

max Z = 5x1 + 4x2

subject to
x1 - 2x2 <= 1
x1 + 2x2 >= 3

x1,x2 >= 0
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
#%%
# function domain
x = np.linspace(0, 10, 20)
#%%
# constraints
eq1 = ( x - 1) / 2  # x2 >=
eq2 = ( 3 - x) / 2  # x2 >=
#%%
# z equation (objective function)
zeq = lambda v, c: (c - 5*v) / 4  # Z = 5*x1 + 4*x2
#%%
# equations 
equations_list = [(x ,eq1),
                  (x, eq2),
                  ]

# labels
equations_label = [r"$x_1 - 2x_2 = 1$",
                   r"$x_1 + 2x_2 = 3$",
                   ]

#%%
plt.figure(figsize=(10,10))

plt.axvline(0, color="0.4")
plt.axhline(0, color="0.4")

# plot equations
for eq, eqlabel in zip(equations_list, equations_label):
    plt.plot(*eq, lw=2, label=eqlabel)

# plot z function
plt.plot(x, zeq(x, 0), lw=3, ls="--", color="magenta", alpha=0.2, label=r"$\max\; Z = 5x_1 + 4x_2$" )
for z in np.linspace(5, 30, 6):
    plt.plot(x, zeq(x, z), lw=3, ls="--", color="magenta", alpha=0.2)
# Constraint areas
plt.fill_between(x, eq1, eq1 + 10, facecolor="blue", alpha=0.3)
plt.fill_between(x, eq2, eq2 + 10, facecolor="orange", alpha=0.3)
plt.xlim(-1, 6)
plt.ylim(-1, 4)
plt.legend(fontsize=12, loc="upper right")
plt.show()

