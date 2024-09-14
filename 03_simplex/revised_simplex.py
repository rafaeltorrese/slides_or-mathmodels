from itertools import combinations
import numpy as np
import pandas as pd

from pprint import pprint
from tabulate import tabulate

from typing import List, Tuple, Union

def get_feasible_solution(matrix, base, rhs):
    inv_base = np.linalg.inv(base)
    return inv_base.dot(matrix), inv_base.dot(rhs)

def optimal_condition_test(profit):
    return  np.all(profit <= 0)

def update_base(profit, matrix, base, rhs,  cj, cb) -> None:
    entering_index = profit.argmax()
    column_key = matrix[:, entering_index]
    
    print(column_key)
    ratios = np.full_like(column_key, np.inf)
    np.divide(rhs, column_key, where=column_key>0, out=ratios)
    leaving_index = ratios.argmin()

    cb[leaving_index] = cj[entering_index]
    base[:, leaving_index] = column_key
    return base, cb, (leaving_index, entering_index)

def get_profit(cj, cb, body):
    return cj - cb.dot(body)


def simplex(
    body: List[list], 
    rhs: list, 
    cj: list, 
    basics: list,  
    direction: int=1
    ):

    matrix = np.array(body, dtype=float)
    body = np.array(body, dtype=float)
    num_equations, num_variables = matrix.shape 

    rhs = np.array(rhs, dtype=float)
    b = np.array(rhs, dtype=float)

    cj = np.array(cj, dtype=float)
    cb = cj[[*basics]]

    profit = get_profit(cj, cb, body)
    optimal = optimal_condition_test(profit)

    base = matrix[:, [*basics]]
    basics_index = ()

    while not optimal:
        base, cb, index = update_base(profit, body, base, rhs, cj, cb)
        basics_index += (index, )

        body, rhs = get_feasible_solution(matrix, base, b)
        profit = get_profit(cj, cb, body)
        optimal = optimal_condition_test(profit)
    print(basics)
    for (leaving, entering) in basics_index:
        basics[leaving] = entering
        print(basics)
    print(rhs)
    print('zvalue')
    print(cj[[*basics]].dot(rhs))   


    


if __name__ == '__main__':
    A = [
        [1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [1, 1, 0, 0, 1, 0],
        [4, 2, 0, 0, 0, 1],
    ]

    b = [
        1_000, 
        1_500, 
        1_750, 
        4_800,
        ]

    c = [
        12,
        9, 
        0, 
        0, 
        0, 
        0,
    ]

    simplex(A, b, c, [2, 3, 4, 5])