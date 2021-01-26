import numpy as np

cj = np.array([45, 40, 85, 65])
bi = np.array([800, 200, 700])
Aij = np.array([[3,4,8,6], [2,2,7,5], [6,4,7,4]])

# arbitrary solution. Choose whatever you want
xi = np.array([10,30,70,20])

# value of the objective function
print(cj.dot(xi))
z = cj.dot(xi)


# left-hand side values
print(Aij.dot(xi))
lhs = Aij.dot(xi)

# compare lhs with rhs. is the solution feasible?
print(lhs >= bi)

