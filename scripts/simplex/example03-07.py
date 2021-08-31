#%% [markdown]
# # Example 03-07
#   $$\max Z = -x_1  +4x_2  $$
#     
#     
#     
#    -3x_1 + x_2 \leq 6,
#       x_1 + 2x_2 \leq 4,
#       x_2 \leq -3
#    
#     no lower bound constraint for $x_1$ 
#%% [markdown]
# ## Import Libraries
import numpy as np
import matplotlib.pyplot as plt
#%% [markdown]
# ## Domain of independent variable
x = np.linspace(-50, 50, 30)

zfunction = lambda z, x: (z  + x )/4
zdomain = np.linspace(-20, 20, 5)
zlabel = r"$Z = -x_1  + 4x_2$"

#%% 
y1 = 6 + 3 * x
y2 = (4 - x) / 2
y3 = np.full_like(x, -3)

ylabels = [
    r"$-3x_1 + x_2 = 6$",
    r"$x_1 + 2x_2 =4$",
    r"$x_2 = -3$",
]

equations = [y1, y2, y3]

# ## Plotting
# ----------------
plt.figure(figsize=(8,8))
colors = ("orange", "green", "red")

plt.subplot(1,2,1)

plt.xlim(-6, 10)
plt.ylim(-6, 10)

plt.axvline(0, color="0.4")
plt.axhline(0, color="0.4")
# Equations (lines)
for y, tag, c in zip(equations, ylabels, colors):
    plt.plot(x, y, lw=3, color=c, label=tag)

# Objective Function
plt.plot(x, zfunction(0, x), lw=2, ls="--", color="magenta", alpha=0.3, label=zlabel)
for z in zdomain:
    plt.plot(x, zfunction(z, x), lw=2, ls="--", color="magenta", alpha=0.3)


plt.legend(fontsize=13, loc="upper right")

# ---------------- SUBPLOT --------------------
plt.subplot(1,2,2)

plt.xlim(-6, 10)
plt.ylim(-6, 10)

plt.axvline(0, color="0.4")
plt.axhline(0, color="0.4")
# Equations (lines)
for y, tag, c in zip(equations, ylabels, colors):
    plt.plot(x, y, lw=3, color=c, label=tag)

# Objective Function
plt.plot(x, zfunction(0, x), lw=2, ls="--", color="magenta", alpha=0.3, label=zlabel)
for z in zdomain:
    plt.plot(x, zfunction(z, x), lw=2, ls="--", color="magenta", alpha=0.3)


plt.fill_between(x, 
                y1, 
                y1 - 20, 
                color=colors[0], 
                alpha=0.3, 
                label=r"$-3x_1 + x_2 \leq 6$")

plt.fill_between(x, 
                y2, 
                y2 - 10, 
                color=colors[1], 
                alpha=0.3, 
                label=r"$x_1 + 2x_2  \leq 4$")

plt.fill_between(x, 
                y3, 
                y3 - 20, 
                color=colors[2], 
                alpha=0.3, 
                label=r"$x_2 \leq -3$")

plt.legend()
plt.show()


