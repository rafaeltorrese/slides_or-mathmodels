# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

## Example 01 ##
# Max Z = 3x1 + 4x2 
# x1 + x2 <= 450
# 2x1 + x2 <= 600



x = np.linspace(-10,500, 50)
eq1 = 450 - x
eq2 = 600 - 2*x
zfunction = lambda z,x:(z - 3*x)/4


plt.figure(figsize=(5,5))
plt.axvline(0, color='gray')
plt.axhline(0, color='gray')
plt.plot(x,eq1, label=r"$x_1 + x_2 \leq 450$")
plt.plot(x,eq2, label=r"$2x_1 + x_2 \leq 600$")
for i in np.linspace(500,1500,4):
    plt.plot(x, zfunction(i,x), color='red', lw=1.2, ls="--", alpha=0.4)



points = [(0,0), (0,450), (150, 300), (300,0)]
zvalue = lambda x,y: 3*x + 4*y
best_index, best_value = max(((i, zvalue(*point)) for i,point in enumerate(points)), key=lambda t:t[1])
best_point = points[best_index]

plt.plot(*best_point, marker="*", ms=10,color="red")
plt.plot(x, zfunction(best_value, x), color='red', ls="--", lw=1.5)

plt.legend()
plt.xlim(-20,500)
plt.ylim(-20,650)
plt.show()