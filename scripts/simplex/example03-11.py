#%% [markdown]
# # Example 11
# $$\max\, Z = −x_1 + 2x_2$$
# $$\begin{align*}
# x 1 − x 2 &\leq −1 \\
# −0.5x_1 + x_2 &\leq 2 \\
# \end{align*}$$
# %%
import numpy as np
import matplotlib.pyplot as plt 
# %%
x = np.linspace(-10, 80, 10)
# %%
objective = {
    'f': lambda z, x: (z + x) / 2,
    'label': r'$\max\, Z = −x_1 + 2x_2$',
    'domain': np.linspace(-6, 3 , 3),
    'color': 'magenta',
    'ls': '--',
}


# %%
y1 = {
    'x': x, 
    'y': x + 1,
    'color':'orange',
    'label1': r'$x_1 − x_2 = −1$',
    'label2': r'$x_1 − x_2 \leq −1$',
}

y2 = {
    'x': x, 
    'y':2 + 0.5 * x,
    'color': 'green',
    'label1': r'$−0.5x_1 + x_2 = 2$',
    'label2': r'$−0.5x_1 + x_2 \leq 2$',
}

# %%
# ## Plotting
# %%
plt.figure(figsize=(10, 10))

# --- SUBPLOT ----
plt.subplot(121)
plt.xlim(-5, 15)
plt.ylim(-5, 15)

plt.axvline(0, color='0.6')
plt.axhline(0, color='0.6')

# lines
for eq in [y1, y2]:
    plt.plot(
            eq['x'],
            eq['y'],
            lw=2,
            color=eq['color'],
            label=eq['label1'],
            )

# z function
plt.plot(
        x,
        objective['f'](0, x),
        lw=3,
        ls=objective['ls'],
        color=objective['color'],
        alpha=0.2,
        label=objective['label']
        )

# z values
for z in objective['domain']:
    plt.plot(
            x,
            objective['f'](z, x),
            lw=3,
            ls=objective['ls'],
            color=objective['color'],
            alpha=0.2,
            )

# areas
plt.fill_between(x, 
                y1['y'], 
                y1['y'] - 10, 
                color=y1['color'], 
                alpha=0.2,
                label=y1['label2'],
                )

plt.fill_between(x, 
                y2['y'], 
                y2['y'] - 10, 
                color=y2['color'], 
                alpha=0.2,
                label=y2['label2'],
                )

plt.legend(fontsize=10, loc='upper right')
# --- SUBPLOT ----
plt.subplot(122)
plt.xlim(-5, 15)
plt.ylim(-5, 15)

plt.axvline(0, color='0.6')
plt.axhline(0, color='0.6')

# lines
for eq in [y1, y2]:
    plt.plot(
            eq['x'],
            eq['y'],
            lw=2,
            color=eq['color'],
            label=eq['label1'],
            )

# z function
plt.plot(
        x,
        objective['f'](0, x),
        lw=3,
        ls=objective['ls'],
        color=objective['color'],
        alpha=0.2,
        label=objective['label']
        )

# zvalues
for z in objective['domain']:
    plt.plot(
            x,
            objective['f'](z, x),
            lw=3,
            ls=objective['ls'],
            color=objective['color'],
            alpha=0.2,
            )

plt.legend(fontsize=10, loc='upper right')
# ---
plt.show()