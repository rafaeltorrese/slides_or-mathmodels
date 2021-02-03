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

points = [(0,0), (0,450), (150, 300), (300,0)]
zvalue = lambda x,y: 3*x + 4*y
best_index, best_value = max(((i, zvalue(*point)) for i,point in enumerate(points)), key=lambda t:t[1])
best_point = points[best_index]
coordinates = list(zip(*points))

# Plot the feasible region
plt.figure(figsize=(5,5))
plt.axis("equal")

plt.axvline(0, color='gray')
plt.axhline(0, color='gray')

plt.plot(x,eq1, lw=3, label=r"$x_1 + x_2 \leq 450$")
plt.plot(x,eq2, lw=3, label=r"$2x_1 + x_2 \leq 600$")

for i in np.linspace(500,1500,4):  # z function lines
    plt.plot(x, zfunction(i,x), color='red', lw=1.5, ls="--", alpha=0.4)
    
for point in points:  # corner points
    plt.plot(*point, marker="o", color="k", ms=7)
    
plt.fill(*coordinates, facecolor="yellow", edgecolor="gray", alpha=0.4) # feasible region

plt.plot(*best_point, marker="*", ms=10,color="red")  # coordinates of the best point
plt.plot(x, zfunction(best_value, x), color='red', ls="--", lw=1.8)  # line plot for the best z function

plt.legend(fontsize=15, loc="upper right")
plt.xlim(-20,500)
plt.ylim(-20,500)
plt.show()