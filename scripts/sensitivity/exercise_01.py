import numpy as np
import pandas as pd


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


print(bsolution)
dirname = r'C:\Users\rafael.torrese\Documents'

# table.to_excel(f'{dirname}\ex01.xlsx')


np.savetxt("ex01.csv", A, delimiter=",")


