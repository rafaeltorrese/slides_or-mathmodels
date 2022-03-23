from cProfile import label
from itertools import combinations

import numpy as np
import pandas as pd


def dual(A, b, z, cbidx=None):
    A = A.astype(float)
    b = b.astype(float)
    z = z.astype(float)
    
    num_equations, num_variables = A.shape
    labels = np.array([f'x_{v}'for v in range(1, num_variables + 1)])
    if cbidx:
        cb_index = cbidx
    else:
        cb_index = np.nonzero((np.abs(M.sum(axis=0)) == 1) & (M.sum(axis=0) == 1))[0]

    cb = z[cb_index]
    zj = cb.dot(A)
    zvalue = cb.dot(b)
    net_evaluation = z - zj

    optimal = np.all(net_evaluation <= 0)
    unfeasible = np.any(b < 0)

    if not optimal:
        print('Method Fails')
        return

    iteration = 0


    while optimal and unfeasible:
        ratios = np.full_like(z, np.inf)        
        leaving_index = b.argmin()  # dual feasibility condition
        pivot_row = A[leaving_index]
        if np.all(pivot_row >= 0):
            print('Unfeasible Solution')
            return
        np.divide(net_evaluation, pivot_row, where=pivot_row < 0, out=ratios)                
        entering_index = ratios.argmin()  # dual optimality condition
        pivot = A[leaving_index, entering_index]        

        entering_label = labels[entering_index] 
        leaving_label = labels[cb_index[leaving_index]]

        print(f'Leaving: {leaving_label}. Entering: {entering_label}')
        if pivot != 1:            
            A[leaving_index] /= pivot
            b[leaving_index] /= pivot

        # Gauss- Jordan
        rows_id = [*range(num_equations)]
        rows_id.pop(leaving_index)
        for i in rows_id:
            target = -A[i, entering_index]            
            A[i] += target * A[leaving_index]
            b[i] += target * b[leaving_index]

        # update        
        cb_index[leaving_index] = entering_index
        cb = z[cb_index]

        zj = cb.dot(A)        
        net_evaluation = z - zj
        zvalue = cb.dot(b)

        optimal = np.all(net_evaluation <= 0)
        unfeasible = np.any(b < 0)        
        iteration += 1

    print(f'Optimal Solution Found.\n Number of iterations: {iteration}')
    print(f'Z value: {zvalue}')




    

if __name__ == '__main__':
    M = np.array([
        [-2, -3, -5, 1, 0, 0,],
        [3, 1, 7, 0, 1, 0,],
        [1, 4, 6, 0, 0, 1,],
    ])

    rhs = np.array([-2, 3, 5])

    cj  = np.array([-2, -2, -4, 0, 0, 0,])

    dual(M, rhs, cj)    