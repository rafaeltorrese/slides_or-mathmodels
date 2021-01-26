import numpy as np

cj = np.array([4, 3, 6])
bi = np.array([440, 470, 430])
Aij = np.array([[2, 3, 2 ], [4, 0, 3], [2, 5, 0]])

# arbitrary solution. Choose whatever you want
xi = np.array([30, 30, 12])

# value of the objective function
print(cj.dot(xi))
z = cj.dot(xi)


# left-hand side values
print(Aij.dot(xi))
lhs = Aij.dot(xi)

# compare lhs with rhs. is the solution feasible?
print(lhs <= bi)

