from tabulate import tabulate
from fractions import Fraction

import numpy as np
import pandas as pd

np.set_printoptions(
    formatter={
        'all': lambda x: str(Fraction(x).limit_denominator())
    }
)

pd.set_option(
    'display.float_format', lambda x: str(Fraction(x).limit_denominator())
)

def simplex(matrix, rhs, z, varlabel='x', direction=1):
    '''Simplex algorithm to solve linear programming problems

    Parameters
    ----------
    matrix: numpy ndarray
        Matrix of coefficients in the left-hand side

    rhs: numpy ndarray
        Right-hand side vector

    direction: {+1 , -1}
        Use +1 for maximization and -1 for minimization.

    Returns
    -------
    solutions: numpy ndarray
        Vector solutions of every iteration

    fvalues: numpy ndarray
        Values of z (objective function)

    lastrows: numpy ndarray
        Last rows of optimal table, this rows corresponde to Zj and cj - Zj
    '''
    print("="*10, "Simplex Method", "="*10)
    matrix =np.array (matrix, dtype=float)
    rhs= np.array (rhs, dtype=float)
    z=np.array (z, dtype=float)
    
    num_rows, num_cols= matrix.shape
    cb_index = np.nonzero((np.abs(matrix).sum(axis=0) == 1) & (matrix == 1))[1]
    cb = z[cb_index]
    
    zj= cb.dot (matrix)
    ner= direction*(z-zj) #ner:net evaluation rot
    
    labels = [f'{varlabel}{i}' for i in range (1, num_cols + 1)]    
    basic_labels = [labels[idx] for idx in cb_index]
    
        
    iteration = 0
    while np.any(ner > 0):
        solution = np.zeros_like(z)
        entering= ner.argmax ()
        entering_label=labels[entering]
        
        key_column= matrix[:, entering]
        
        ratios=np.full_like (rhs, np.inf)
        np.divide (rhs, key_column, where=key_column>0, out=ratios)
        
        leaving= ratios.argmin()
        leaving_label=labels[cb_index[leaving]]
        
        pivot=matrix[leaving, entering]
        
        if pivot !=1:
            matrix [leaving]=matrix [leaving]/pivot
            rhs [leaving]=rhs[leaving]/pivot
            
        #Gauss-Jordan
        for i in range (num_rows):
            if i != leaving:
                factor = matrix [i, entering]
                matrix [i]=-factor * matrix [leaving] + matrix[i]
                rhs [i]=-factor * rhs [leaving] + rhs [i]
                
        basic_labels[leaving] = entering_label
        cb_index[leaving] = entering
        cb = z[cb_index]
        zj = cb.dot(matrix)
        ner = direction*(z-zj)
        
        iteration+=1
        zvalue = cb.dot(rhs)
        
        print (f'Iteration {iteration}. \nIn:{entering_label}. Out:{leaving_label}')
        
        print(
            tabulate(
                np.hstack((matrix, rhs[:, np.newaxis])),
                headers=labels+['b'],
                showindex=basic_labels,
#                 numalign='decimal',
#                 disable_numparse=True,
#                 floatfmt=Fraction().limit_denominator(),                
#                 tablefmt='pipe',
#                 tablefmt='pretty',
                tablefmt='orgtbl',
#                 tablefmt='github',
                floatfmt='.3f',
            ),
            '\n',
        )
        print(
            tabulate(
                np.vstack((zj, direction * ner)),
                showindex=['zj', 'cj-zj'],
                headers=labels,
                tablefmt='grid',
            ),
            '\n'
        )
                    
        
        if np.all (ner<=0):
            print (f'Optimal solution found in {iteration} iteration(s)')
            print(
                tabulate(
                    {
                        'Basics': basic_labels, 
                        'Values': rhs,
                    },
                    headers='keys',
#                     tablefmt='github',
#                     tablefmt='pipe',
#                     tablefmt='tsv',
                    tablefmt='orgtbl',
#                     tablefmt='psql',
#                     tablefmt='pretty',
#                     floatfmt='.3f',
                )
             )
            print(f'Zvalue: {zvalue.round(2)}')
            
    return pd.DataFrame({'index': cb_index, 'cb': cb}, index=basic_labels),\
pd.DataFrame(np.vstack((matrix, zj, direction * ner)), columns=labels, index=basic_labels + ['zj', 'cj-zj']),\
pd.Series(np.append(rhs, zvalue), index=basic_labels + ['z'], name='Solution')      


if __name__ == '__main__':
    Aprimal = [
        [6, 4, 1, 0, 0, 0],
        [1, 2, 0, 1, 0, 0],
        [-1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1],
    ]

    bprimal = [24, 6, 1, 2]

    Zvector = [5, 4, 0, 0, 0, 0]    

    basis, main, sol = simplex(matrix=Aprimal, rhs=bprimal,
                                                       z=Zvector,  direction=1)
    print()
    print(basis)
    print(
        '\n',
        main.rename(
            columns={
                'x5': 's1',
                'x6': 's2',
                'x7': 's3',
                'x8': 'A1',
                'x9': 'A2',
                'x10': 'A3',
            },
            #     inplace=True,
        )
    )
    print(
        '\n',
        sol
    )

