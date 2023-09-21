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

def gauss_jordan(Matrix, leaving_index, entering_index):
    Matrix = np.array(Matrix)
    pivot = Matrix[leaving_index, entering_index]
    if pivot != 1:
        np.divide(Matrix[leaving_index], pivot, out=Matrix[leaving_index])
    for index_row, current_row in enumerate(Matrix):
        if index_row == leaving_index:
            continue        
        target = current_row[entering_index]
        if target == 0:
            continue
        new_row = current_row - target * Matrix[leaving_index]
        Matrix[index_row] = new_row
    return Matrix

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

def simplex_algorithm_01(Matrix, sense=1):
    'Taha Version'
    table = np.array(Matrix)
    iterations = {}
    iteration_id = 0
    objective_coefficients = sense * table[0, 1:-1]
    while np.any(objective_coefficients < 0):
        iteration_id += 1
        solution_column = table[1:, -1]

        entering  = objective_coefficients.argmin() + 1
        entering_column = table[1:, entering]

        ratios = np.full_like(A[1:, -1], np.inf)
        np.divide(solution_column, entering_column, where=entering_column>0, out=ratios)
        leaving = ratios.argmin() + 1

        print(f'Iteration: {iteration_id}. Leaving: {leaving}. Entering: {entering}')

        table = gauss_jordan(table, leaving, entering)
        objective_coefficients = sense * table[0, 1:-1]

        name_table = f'iter{str(iteration_id).zfill(2)}'
        iterations[name_table] = table

    print(f'Optimal Solution Found. Iterations {iteration_id}')
    return iterations

def simplex_algorithm_02(Matrix, z, initial_basics_index, sense=1):
    'Reduced Costs Version'
    table = np.array(Matrix, dtype=float)
    cj = np.array(z, dtype=float)

    iterations = {}
    iteration_id = 0

    cb = cj[initial_basics_index]   
    zj = cb.dot(table[:, :-1])
    net_evaluation_row = cj - zj
    solution_column = table[:, -1]  # last column of the Simplex Table
    while np.any(sense *  net_evaluation_row > 0):
        iteration_id += 1
        
        entering  = net_evaluation_row.argmax()   # index of entering variable
        entering_column = table[:, entering]
        
        ratios = np.full_like(solution_column, np.inf)
        np.divide(solution_column, entering_column, where=entering_column>0, out=ratios)
        leaving = ratios.argmin()  # index of leaving variable

        table = gauss_jordan(table, leaving, entering)        
        solution_column = table[:, -1]  # last column of the Simplex Table

        cb[leaving] = cj[entering]   
        zj = cb.dot(table[:, :-1])
        net_evaluation_row = cj - zj

        zvalue = cb.dot(solution_column)

        print(f'Iteration: {iteration_id}. Leaving: {leaving}. Entering: {entering}. Z = {zvalue}')
        name_table = f'iter{str(iteration_id).zfill(2)}'
        net_evaluation_augmented = np.append(net_evaluation_row, zvalue).reshape(1, -1)
        iterations[name_table] = np.concatenate([table, cb.dot(table).reshape(1,-1), net_evaluation_augmented])

    print(f'Optimal Solution Found in {iteration_id} Iteration(s) ')
    
    return iterations

if __name__ == '__main__':
    Aprimal = [
        [6, 4,  1, 0, 0, 0, 24],
        [1, 2,  0, 1, 0, 0, 6],
        [-1, 1, 0, 0, 1, 0, 1],
        [0,  1, 0, 0, 0, 1, 2],
    ]

    bprimal = [24, 6, 1, 2]

    Zvector = [5, 4, 0, 0, 0, 0]    

    tables = simplex_algorithm_02(Matrix=Aprimal, 
                                  z=Zvector, 
                                  initial_basics_index=[2, 3, 4, 5], 
                                  sense=1,
                                  )
    
    print(tabulate(
        tables['iter02'],
        headers='x1 x2 s1 s2 s3 s4 solution'.split(),
        tablefmt='github',
    ))

    basic_labels_index = np.where(tables['iter02'][-2, :-1] == Zvector)[0]
    label_variables = 'x1 x2 s1 s2 s3 s4'.split()
    print([label_variables[basic] for basic in basic_labels_index])

