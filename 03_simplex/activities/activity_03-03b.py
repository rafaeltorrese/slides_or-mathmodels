#%%
import numpy as np
import pandas as pd
#%%
from simplex_algorithm import simplex
#%%
if __name__ == '__main__':

    zvector = np.array(
        [3, 4, 0, 0, 0, 0, -10_000, -10_000]
    )

    A = np.array(
        [
            [5, 4, 1, 0,  0,  0, 0, 0],
            [3, 5, 0, 1,  0,  0, 0, 0],
            [5, 4, 0, 0, -1,  0, 1, 0],
            [8, 4, 0, 0,  0, -1, 0,  1],
        ]
    )

    

    b = np.array(
        [200, 150, 100, 80]
    )

    
    
    basis_list = simplex(A=A, rhs=b, cj=zvector, direction=1)
    



