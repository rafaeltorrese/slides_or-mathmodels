#%% [markdown]
# # Reddy Mikks
# Reddy Mikks produce pinturas para interiores y exteriores con dos materias primas, $M1$ y $M_2$. La tabla siguiente proporciona los datos básicos del problema.
#
# |                                 | Pintura para exteriores | Pintura para interiores | Disponibilidad (toneladas) |
# |---------------------------------|-------------------------|-------------------------|----------------------------|
# | Materia prima $M_1$             | 6                       | 4                       | 24                         |
# | Materia prima $M_2$             | 1                       | 2                       | 6                          |
# | Utilidad por tonelada (\\$1000) | 5                       | 4                       |                            |
#
# ## Model
#
# $$\max z = 5x_1 + 4x_2$$
# s.t.
# $$\begin{align*}
# 6x_1 + 4x_2  & \leq 24 \\
# x_1 + x_2 & \leq 6\\
# -x_1 + x_2 & \leq 1\\
# x_2  & \leq 2\\
# x_1, x_2 & \geq 0\\    
# \end{align*}$$
# 

# %%
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
# %% [markdown]
# ## Domain Function
x = np.linspace(0, 100, 50)
print(x.shape)
#%% [markdown]
# ## Objective Function 
zfunction = lambda z, x: (z - 5 * x) / 4
zlabel = r"$Z = 5x_1 + 4x_2$"
zdomain = np.linspace(5, 20, 5)
# %% [markedown]
# ## Equations
equation1 = (24 - 6 * x) / 4
equation2 = (6 - x) / 2
equation3 = 1 + x
equation4 = np.full_like(x, 2)  #  it's a constant

#%% [markdown]
labels = [
    r"$6x_1 + 4x_2 \leq 24$",
    r"$x_1 + 2x_2 \leq 6$",
    r"$-x_1 + x_2 \leq 1$",
    r"$x-2 \leq 2$",
]

# %%
equations = [
    equation1, 
    equation2, 
    equation3, 
    equation4,
    ]
# %% [markdown]
# ## Plotting
plt.figure(figsize=(10, 10))
plt.xlim(-1, 7)
plt.ylim(-1, 7)

plt.axvline(0, color="0.4")
plt.axhline(0, color="0.4")

plt.plot(x, equation4)

# Plot lines: x, f(x)
for equation, label in zip(equations, labels):
    plt.plot(x, equation, lw=2, label=label)

# Plot z values
plt.plot(x, zfunction(0, x), color="magenta", ls="--", label=zlabel, alpha=0.3)
for z in zdomain:
    plt.plot(x, zfunction(z, x), ls="--", color="magenta", alpha=0.3)

plt.fill_between(x, equation1, where=(x < equation1), color="orange", alpha=0.2, interpolate=True)
plt.fill_between(x, equation2, where=(x <= equation2), color="green", alpha=0.2, interpolate=True)
plt.fill_between(x, equation4, color="blue", alpha=0.2, interpolate=True)

plt.legend(
    fontsize=15, 
    loc="upper right"
    )
plt.show()


# %%
