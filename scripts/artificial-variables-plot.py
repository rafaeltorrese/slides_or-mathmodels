# %%
import numpy as np
import matplotlib.pyplot as plt
# %%
# %%
x = np.linspace(-5, 100, 50)
# %%
zeq = {
    'f': lambda z, x: (z - 12 * x) / 20,
    'label': r'$\min\, Z = 12x_1 + 20x_2$',
    'domain': np.linspace(500, 250, 5),
    'color': 'magenta',
    'ls': '--',
}

y1 = {
    'x': x,
    'y': (100 - 6 * x) / 8,
    'color': 'blue',
    'label1': r'$6x_1 + 8x_2 = 100$',
    'label2': r'$6x_1 + 8x_2 \geq 100$'
}

y2 = {
    'x': x,
    'y': (120 - 7 * x) / 12,
    'color': 'orange',
    'label1': r'$7x_1 + 12x_2 = 120$',
    'label2': r'$7x_1 + 12x_2 \geq 120$',
}
# %% [markdown]
# ## Plotting
# %%
plt.figure(figsize=(10, 10))

# -------- SUBPLOT --------------
plt.subplot(121)
plt.xlim(-1, 20)
plt.ylim(-1, 20)

plt.axvline(0, color='0.3')
plt.axhline(0, color='0.3')

# lines
for L in [y1, y2]:
    plt.plot(L['x'], L['y'], color=L['color'], lw=2, label=L['label1'])

# z function
plt.plot(x, zeq['f'](600, x),
         lw=3,
         ls=zeq['ls'],
         color=zeq['color'],
         alpha=0.2,
         label=zeq['label'],
         )
# z valules
for z in zeq['domain']:
    plt.plot(x, zeq['f'](z, x),
             lw=3,
             ls=zeq['ls'],
             color=zeq['color'],
             alpha=0.2,
             )
# areas
plt.fill_between(x, y1['y'], y1['y'] + 10,
                 color=y1['color'],
                 alpha=0.2,
                 label=y1['label2'],
                 )

plt.fill_between(x, y2['y'], y2['y'] + 10,
                 color=y2['color'],
                 alpha=0.2,
                 label=y2['label2'],
                 )
# legend
plt.legend(fontsize=10, loc='upper right')
# -------- SUBPLOT --------------
plt.subplot(122)

plt.xlim(-1, 20)
plt.ylim(-1, 20)

plt.axvline(0, color='0.3')
plt.axhline(0, color='0.3')

# lines
for L in [y1, y2]:
    plt.plot(L['x'], L['y'], color=L['color'], lw=2, label=L['label1'])

# z function
plt.plot(x, zeq['f'](600, x),
         lw=3,
         ls=zeq['ls'],
         color=zeq['color'],
         alpha=0.3,
         label=zeq['label'],
         )
# z valules
for z in zeq['domain']:
    plt.plot(x, zeq['f'](z, x),
             lw=3,
             ls=zeq['ls'],
             color=zeq['color'],
             alpha=0.3,
             )
# legend
plt.legend(fontsize=10, loc='upper right')
# ------
plt.show()
