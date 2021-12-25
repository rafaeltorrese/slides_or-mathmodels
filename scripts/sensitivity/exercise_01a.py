from fractions import Fraction
import numpy as np
import pandas as pd
np.set_printoptions(formatter={'all': lambda x: str(Fraction(x).limit_denominator())})

from simplex_algorithm import simplex

A = np.array(
    [
        [8, 3, 4, 1, 1, 0, 0], 
        [2, 6, 1, 5, 0, 1, 0],
        [1, 4, 5, 2, 0, 0, 1],
        ]
)

b = np.array([7, 3, 8])

zvector = np.array([3, 4, 1, 7, 0, 0, 0])

sols, lastrows, table, bsolution, cbindx = simplex(matrix=A, rhs=b,
                                                       z=zvector,   direction=1)

labels = 'x1 x2 x3 x4 s1 s2 s3'.split()                                                       
label_basis = [labels[i] for i in cbindx]

print('Last Rows\n', lastrows, '\n')
print(f'Basis: {label_basis}\n')
print(bsolution.to_numpy(), '\n')

print(zvector[cbindx])
print(np.dot(bsolution.to_numpy(), zvector[cbindx]))
dirname = r'C:\Users\rafael.torrese\Documents'



# table.to_excel(f'{dirname}\ex01.xlsx')


# np.savetxt("ex01.csv", A, delimiter=",")

base = A[:, cbindx]
base_inv = np.linalg.inv(base)

print('Inverse of Base Matrix\n', base_inv)


