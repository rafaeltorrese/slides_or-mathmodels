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
# %%
x = np.linspace(0, 100, 50)



