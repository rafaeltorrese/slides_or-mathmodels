#%% [markdown]
# $$\min\, z = 5x_1 + 8x_2$$

# $$\begin{align*}
# x_1 &\leq 4 \\
# x_2 &\geq 2\\
# x_1 + x_2 &= 5\\
# x_1, x_2 &\geq 0
# \end{align*}$$
# %% 
import numpy as np
import matplotlib.pyplot as plt
# %%
x = np.linspace(-10,100, 10)
print(x)
print(x[x<4])
# %%
objective = {
    'function': lambda z, x: (z - 5 * x) / 8,
    'domain': np.linspace(60, 45, 3),
    'label': r'$\min\, z = 5x_1 + 8x_2$',
}

# %%
expr1 = {
    'x': [4, 4],
    'y': [-1, 100],
    'label': r'$x_1 = 4$',
    'label2': r'$x_1 \leq 4$',
    'color': 'orange',
    'index': 0
}

expr2 = {
    'x': [-1, 100],
    'y': [2, 2],
    'label': r'$x_2 = 2$',
    'label2': r'$x_2 \geq 2$',
    'color': 'green',
    'index': 1,
}

expr3 = {
    'x': x,
    'y': 5 - x,
    'label': r'$x_1 + x_2 = 5$',
    'color': 'red',
    'index': 2,
}


# %% [markdown]
# ## Plotting
# %%

plt.figure(figsize=(8,8))
# ------- SUBPLOT -----------
plt.subplot(121)
plt.xlim(-1, 7)
plt.ylim(-1, 7)

plt.axvline(0, color="0.5")
plt.axhline(0, color="0.5")

# lines
for line in [expr1, expr2, expr3]:
    plt.plot(
        line['x'],
        line['y'],
        lw=3,
        color=line['color'],
        label=line['label'],
            )
# z function            
plt.plot(
        x,
        objective['function'](38, x),
        lw=3,
        ls='--',
        color='magenta',
        label=objective['label'],
        alpha=0.2,        
        )
# z function
for z in objective['domain']:
    plt.plot(
            x,
            objective['function'](z, x),
            lw=3,
            ls='--',
            color='magenta',
            alpha=0.2,        
            )
# areas
plt.fill_between(
                [-1, 4],
                50,
                -10,
                color='orange',
                alpha=0.15,
                label=expr1['label2']
)

plt.fill_between(
            [-1, 100],
            2,
            100,
            color='green',
            alpha=0.15,
            label=expr2['label2']
)


plt.legend(fontsize=10, loc='upper right')
# ------- SUBPLOT -----------
plt.subplot(122)
plt.xlim(-1, 7)
plt.ylim(-1, 7)

plt.axvline(0, color="0.5")
plt.axhline(0, color="0.5")

# lines
for line in [expr1, expr2, expr3]:
    plt.plot(
        line['x'],
        line['y'],
        lw=3,
        color=line['color'],
        label=line['label'],
            )

 # z function           
plt.plot(
        x,
        objective['function'](38, x),
        lw=3,
        ls='--',
        color='magenta',
        label=objective['label'],
        alpha=0.2,        
        )

# z's
for z in objective['domain']:
    plt.plot(
            x,
            objective['function'](z, x),
            lw=3,
            ls='--',
            color='magenta',
            alpha=0.2,        
            )

plt.legend(fontsize=10, loc='upper right')
# --------
plt.show()

# %% [markdown]
# ## Solving Linear System Equations
# %%
