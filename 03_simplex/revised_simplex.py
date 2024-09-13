from itertools import combinations
import numpy as np
import pandas as pd

from pprint import pprint
from tabulate import tabulate

from typing import List, Tuple, Union

def get_feasible_solution():
    update_base()
    body = np.linalg.inv(base).dot(matrix)

def optimal_condition_test(profit):
    return  np.all(profit <= 0)

def update_base() -> None:
    entering_index = profit.argmax()
    column_key = body[:, entering_index]
    ratios = np.full_like(rhs, np.inf)
    np.divide(rhs, column_key, where=column_key>0, out=ratios)
    leaving_index = ratios.argmin()

    cb[leaving_index] = cj[entering]
    base[:, leaving_index] = body[:, entering_index]

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
    body = np.full_like(matrix, None)
    num_equations, num_variables = matrix.shape 

    rhs = np.array(rhs, dtype=float)
    cj = np.array(cj, dtype=float)
    cb = cj[[*basics]]
    print(cb)

    profit = get_profit(cj, cb, body)
    optimal = optimal_condition_test(profit)
    print(optimal)

    


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