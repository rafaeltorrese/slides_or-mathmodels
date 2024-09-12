#%%
from itertools import combinations
import numpy as np
from pprint import pprint

#%%
def analytical(lhs, rhs, z, labels, sense=1):    
    A = np.array(lhs, dtype=float)
    num_equations, num_variables = A.shape
    b = np.array(rhs, dtype=float)
    c = np.array(z, dtype=float)
    labels = np.array(labels)
    
    print(f'Dimension of matrix A is: {A.shape}')

    best_solution = {'z': sense * -np.inf}    
    list_basis = [*combinations(range(num_variables), num_equations)]
    print(f'Number of basic solutions: {len(list_basis)}')

    for columns in list_basis:
        try:                 
            base = A[:, [*columns]]            
            x = np.linalg.solve(base, b)
            basic_labels = labels[[*columns]]
            feasible_solution = np.all(x >= 0)     
            if feasible_solution:                                
                zvalue = c[[*columns]].dot(x)                            
                if (sense * zvalue) > best_solution.get('z'):
                    best_solution.update({'z': zvalue})
                    best_solution.update(dict.fromkeys(labels, 0))                                    
                    variables = dict(zip(basic_labels, x))        
                    best_solution.update(variables)                    
        except np.linalg.LinAlgError as e:
            print(f'\nSystem {basic_labels} is {e}')
    print('\nThe best solution is:')
    pprint(best_solution)

#%%
if __name__ == '__main__':
        
    left_hand = [
        [ 6, 4, 1, 0, 0, 0],
        [ 1, 2, 0, 1, 0, 0],
        [-1, 1, 0, 0, 1, 0],
        [ 0, 1, 0, 0, 0, 1],
    ]

    right_hand = [24, 6, 1, 2]
    objective = [5, 4, 0, 0, 0, 0]

    analytical(
        lhs=left_hand, 
        rhs=right_hand, 
        z=objective,
        labels='x1 x2 s1 s2 s3 s4'.split(),
        sense=+1
    )