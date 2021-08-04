import numpy as np

# coefficients of objective function
cj = np.array([90, 280, 40])  
# right-hand side
bi = np.array([0.98, 8, 450, 1]) 
# body matrix (technological coefficients)
Aij = np.array([[0.92, 0.97, 1.04], [7,13,16], [440,490,480], [1,1,1]]) 

# arbitrary solution. Choose whatever you want
xi = np.array([0.10, 0.40, 0.50]) # [0.10, 0.85, 0.05]

# value of the objective function
print(cj.dot(xi))
z = cj.dot(xi)

# left-hand side values
print(Aij.dot(xi))
lhs = Aij.dot(xi)

# compare lhs with rhs. is the solution feasible?
num_rows = Aij.shape[0]  # len(Aij)
print(f'Number of constraints: {num_rows}')
print(lhs[0] <= bi[0])
print(lhs[1] >= bi[1])
print(lhs[2] >= bi[2])
print(lhs[3] == bi[3])
