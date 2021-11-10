from fractions import Fraction
import numpy as np
import pandas as pd
np.set_printoptions(formatter={'all': lambda x: str(Fraction(x).limit_denominator())})

from simplex_algorithm import simplex

A = np.array(
    [[8, 3, 4, 1, 1, 0, 0], 
    [2, 6, 1, 5, 0, 1, 0],
    [1, 4, 5, 2, 0, 0, 1],]
)

b = np.array([7, 3, 8])

zvector = np.array([3, 4, 1, 7, 0, 0, 0])

sols, lastrows, table, bsolution, cbindx = simplex(matrix=A, rhs=b,
                                                       z=zvector,   direction=1)

print('Last Rows\n', lastrows, '\n')
print(bsolution, '\n')
dirname = r'C:\Users\rafael.torrese\Documents'

# table.to_excel(f'{dirname}\ex01.xlsx')


# np.savetxt("ex01.csv", A, delimiter=",")

base = A[:, cbindx]
base_inv = np.linalg.inv(base)

print('Inverse of Base Matrix\n', base_inv)


