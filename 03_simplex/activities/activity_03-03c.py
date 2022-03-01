#%%
import numpy as np
import pandas as pd
#%%
from gurobipy import GRB
#%%
from simplex_algorithm import simplex
#%% [markdown]
# $$\min Z = 45x_1 + 40x_2 + 85x_3 + 65x_4   $$
# subject to
# \begin{align*}
# 3x_1 + 4x_2 + 8x_3 + 6x_4 &\geq  800\\
# 2x_1 + 2x_2 + 7x_3 + 5x_4 &\geq 200\\
# 6x_1  +4x_2 + 7x_3 + 4x_4 & \geq 700\\[5mm]
# x_1, x_2, x_3, x_4 &\geq 0
# \end{align*}

#%%
if __name__ == '__main__':

    z1 = np.array(
        [0, 0, 0, 0, 0, 0, 0,   1, 1, 1,]
    )

    z2 = np.array(
        [45, 40, 85, 65, 0, 0, 0,   10_000, 10_000, 10_000,]
    )
 


    A1 = np.array(
        [
            [ 3, 4, 8, 6, -1,  0,  0, 1, 0, 0,],
            [ 2, 2, 7, 5,  0, -1,  0, 0, 1, 0,],
            [ 6, 4, 7, 4,  0,  0, -1, 0, 0, 1,],            
        ]
    )

    

    b1= np.array(
        [800, 200, 700]
    )

    
    
    basis_list, A2, b2 = simplex(A=A1, rhs=b1, cj=z1, direction=-1)

    basis2, A3, b3 = simplex(A=A2, rhs=b2, cj=z2, direction=-1, cbidx=basis_list[-1].tolist())
    



