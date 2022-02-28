#%%
from cmath import inf
from matplotlib.pyplot import axis
import numpy as np
import pandas as pd
#%%
def simplex(mat, rhs, cj, direction=1):
    mat = mat.astype(float)
    rhs = rhs.astype(float)
    cj = cj.astype(float)

    num_equations, num_variables = A.shape

    I = np.eye(num_equations)
    mask = np.isin(mat, I)
    
    cb_index = np.nonzero(mask.all(axis=0))[0]
    cb = zvector[cb_index]

    zj = cb.dot(mat)    
    net_profit = direction * (cj - zj)

    while np.any(net_profit > 0):
        ratios = np.full(num_equations, np.inf)

        entering_idx = net_profit.argmax()
        key_column = A[:, entering_idx]
        np.divide(rhs, key_column, out=ratios, where=key_column > 0)

        leaving_idx = ratios.argmin()

        pivot = A[leaving_idx, entering_idx]

        if pivot != 1:
            A[leaving_idx] /= pivot
            rhs[leaving_idx] /= pivot
        

        
    
    
    
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
        [5, 4, 0, 0, 0, 0,]
    )

    A = np.array(
        [
            [ 6,  4, 1, 0, 0, 0,],
            [ 1,  2, 0, 1, 0, 0,],
            [-1,  1, 0, 0, 1, 0,],
            [ 0, -2, 0, 0, 0, 1,],
        ]
    )

    

    b = np.array(
        [24, 6, 1, 2]
    )

    
    
    simplex(mat=A, rhs=b, cj=zvector, direction=1)
    



