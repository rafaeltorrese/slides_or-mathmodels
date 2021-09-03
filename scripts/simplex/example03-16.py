#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
x = np.linspace(-10, 50, 20)
#%%
objective = {
    'f': lambda z, x: (z + x) / 2,
    'label': r'$\max\, Z = 3x_1 + 4x_2$',
    'domain': np.linspace(-11, -6 , 3),
    'color': 'magenta',
    'ls': '--',
}
#%%
y1 = {
    'x': x, 
    'y': x,
    'color':'orange',
    'label1': r'$x_1 − x_2 = 0$',
    'label2': r'$x_1 − x_2 \leq 0$',
}

y2 = {
    'x': x, 
    'y': 2.5 * x  + 3,
    'color': 'green',
    'label1': r'$2.5x_1 - x_2 = -3$',
    'label2': r'$2.5x_1 - x_2 \leq -3$',
}
#%%
plt.figure(figsize=(10, 10))

# ----- SUBPLOT -----
plt.subplot(121)

plt.title('Infeasible solution')
plt.xlim(-5, 6)
plt.ylim(-5, 6)

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


# zfunction
plt.plot(
    x,
    objective['f'](-10, x),
    ls=objective['ls'],
    color=objective['color'],
    lw=3,
    alpha=0.2,
    label=objective['label'],
)
# z values
for z in objective['domain']:
    plt.plot(
        x,
        objective['f'](z, x),
        ls=objective['ls'],
        color=objective['color'],
        lw=3,
        alpha=0.2,
    )
# areas
plt.fill_between(
    y1['x'],
    y1['y'],
    y1['y'] - 5,
    color=y1['color'],
    alpha=0.2,
    label=y1['label2'],
)

plt.fill_between(
    y2['x'],
    y2['y'],
    y2['y'] - 10,
    color=y2['color'],
    alpha=0.2,
    label=y2['label2'],
)
# legends
plt.legend(fontsize=10, loc='upper right')
# ----- SUBPLOT
plt.subplot(122)

plt.xlim(-5, 6)
plt.ylim(-5, 6)

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


# zfunction
plt.plot(
    x,
    objective['f'](-10, x),
    ls=objective['ls'],
    color=objective['color'],
    lw=3,
    alpha=0.2,
    label=objective['label'],
)
# z values
for z in objective['domain']:
    plt.plot(
        x,
        objective['f'](z, x),
        ls=objective['ls'],
        color=objective['color'],
        lw=3,
        alpha=0.2,
    )
plt.show()