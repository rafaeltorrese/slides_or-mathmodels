from fractions import Fraction
import numpy as np
import pandas as pd
np.set_printoptions(formatter={'all': lambda x: str(Fraction(x).limit_denominator())})

from simplex_algorithm import simplex

A = np.array(
    [
        [2, 2, 1, 0, 0], 
        [1, 2, 0, 1, 0],
        [4, 2, 0, 0, 1],
        ]
)

b = np.array([160, 120, 280])

zvector = np.array([1, 1.5, 0, 0, 0])

sols, lastrows, table, bsolution, cbindx = simplex(matrix=A, rhs=b,
                                                       z=zvector,   direction=1)

labels = 'x1, x2 s1 s2 s3'.split()
label_basis = [labels[i] for i in cbindx]
print(f'Basis: {label_basis}')
print('Last Rows\n', lastrows, '\n')
print(bsolution, '\n')
dirname = r'C:\Users\rafael.torrese\Documents'

# table.to_excel(f'{dirname}\ex01.xlsx')


# np.savetxt("ex01.csv", A, delimiter=",")

base = A[:, cbindx]
base_inv = np.linalg.inv(base)

print('Inverse of Base Matrix\n', base_inv)


