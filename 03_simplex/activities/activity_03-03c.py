#%%
import numpy as np
import pandas as pd
#%%
from simplex_algorithm import simplex
#%%
def optimality_test():
    zj = cb.dot(mat)    
    net_profit = cj - zj
    if np.all(direction * net_profit <= 0 ):
        print('Optimal solution found')
    else:
        print('Iteration')

def get_basis():
    num_equations, num_variables = A.shape
    I = np.eye(num_equations)
    mask = np.isin(A, I)
    cb_index = np.nonzero(mask.all(axis=0))[0]
    cb = zvector[cb_index]
    return cb_index, cb


#%%
if __name__ == '__main__':

    zvector = np.array(
        [2, 1, 0, 0, 0, 0,]
    )

    A = np.array(
        [
            [ 1,  2, 1, 0, 0, 0,],
            [ 1,  1, 0, 1, 0, 0,],
            [ 1, -1, 0, 0, 1, 0,],
            [ 1, -2, 0, 0, 0, 1,],
        ]
    )

    

    b = np.array(
        [10, 6, 2, 1]
    )

    
    
    basis_list = simplex(A=A, rhs=b, cj=zvector, direction=1)
    



