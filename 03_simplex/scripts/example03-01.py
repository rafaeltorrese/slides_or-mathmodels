"""
Max Z = 3x1 + 4x2 
x1 + x2 <= 450
2x1 + x2 <= 600

x1, x2 >= 0
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,500, 50)

eq1 = 450 - x    # x2 = 450 - x1
eq2 = 600 - 2*x  # x2 = 600 - 2x1
zeq = lambda x1,z:(z - 3*x)/4  # x2 = (Z - 3x1)/4

# ======================================================================
# Plot 
plt.figure(figsize=(5,5))
plt.axis("equal")

plt.axvline(0, color='gray')
plt.axhline(0, color='gray')

plt.plot(x,eq1, lw=3, label=r"$x_1 + x_2 \leq 450$")
plt.plot(x,eq2, lw=3, label=r"$2x_1 + x_2 \leq 600$")

plt.plot(x, zeq(x, 0), color='magenta', ls="--", lw=2, alpha=0.4, label=r"$\max\, Z = 3x_1 + 4x_2$")  # line plot for the best z function
for i in np.linspace(500, 1500, 4):  # z function lines
    plt.plot(x, zeq(x,i), color='magenta', lw=2, ls="--", alpha=0.4)
        
plt.legend(fontsize=12, loc="upper right")
plt.xlim(-10,500)
plt.ylim(-10,500)
plt.show()
# ======================================================================
points = [(0,0), (0,450), (150, 300), (300,0)]  # intersecting points
zvalues = [3*x1 + 4*x2 for x1,x2 in points]
best_index, best_value = max(enumerate(zvalues), key=lambda t:t[1])
best_point = points[best_index]
coordinates = list(zip(*points))

# ======================================================================
# Plot the feasible region
plt.figure(figsize=(5,5))
plt.axis("equal")

plt.axvline(0, color='gray')
plt.axhline(0, color='gray')

plt.plot(x,eq1, lw=3, label=r"$x_1 + x_2 \leq 450$")
plt.plot(x,eq2, lw=3, label=r"$2x_1 + x_2 \leq 600$")

for i in np.linspace(500,1500,4):  # z function lines
    plt.plot(x, zeq(x,i), color='magenta', lw=2, ls="--", alpha=0.4)
    
for point in points:  # corner points
    plt.plot(*point, marker="o", color="k", ms=7)
    
plt.fill(*coordinates, facecolor="yellow", edgecolor="gray", alpha=0.4) # feasible region

plt.plot(*best_point, marker="*", ms=10,color="red")  # coordinates of the best point
plt.plot(x, zeq(x, best_value), color='magenta', ls="--", lw=1.8, label=r"$\max\, Z = 3x_1 + 4x_2$")  # line plot for the best z function

plt.legend(fontsize=12, loc="upper right")
plt.xlim(-10,500)
plt.ylim(-10,500)
plt.show()