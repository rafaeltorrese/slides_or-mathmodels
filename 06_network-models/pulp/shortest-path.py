"""
Chapter 10. Network Models. Shortest Path.
Anderson, David R., Dennis J. Sweeney,
Thomas A. Williams,
Jeffrey D. Camm y Kipp Martin
Quantitative Methods for Business, 11a. Ed
"""
from itertools import product
import math

import pulp as pl

nodes = range(6)


# adjacency_matrix
a = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0],
    ]

costs = [
   [1_000, 25, 20,1_000,1_000,1_000],
   [1_000,1_000, 3, 5,1_000, 14],
   [1_000, 3,1_000,1_000, 6,1_000],
   [1_000, 5,1_000,1_000, 4, 4],
   [1_000,1_000, 6, 4,1_000, 7],
   [1_000,1_000,1_000,1_000,1_000,1_000],
    ]

load = {
    0: 1, 
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: -1,
}



costs = pl.makeDict((nodes, nodes), costs, 1_000)


# problem
problem = pl.LpProblem('shortest', pl.LpMinimize)


# variables
path = pl.LpVariable.dicts('path', (nodes, nodes), 0, None, pl.LpContinuous)

# objective function
problem += pl.lpSum(costs[i][j] * path[i][j] for j in nodes for i in nodes), 'sum_time_path'


# Transhipment Constraints
for k in nodes:
    problem += pl.lpSum(a[k][out] * path[k][out] for out in nodes) - pl.lpSum(a[enter][k] * path[enter][k] for enter in nodes) == load[k], f'path_to_node_{k}'

solver = pl.get_solver('GUROBI') 
problem.solve(solver)

# The status of the solution is printed to the screen
print("Status:", pl.LpStatus[problem.status])


# Each of the variables is printed with it's resolved optimum value
for v in problem.variables():
    if v.varValue > 1e-10:
        print(f'{v.name}: {v.varValue:,.2f}')

print(f'Total Miles = {pl.value(problem.objective):,.2f}')
