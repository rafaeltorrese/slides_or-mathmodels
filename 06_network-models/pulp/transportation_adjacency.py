import pulp as pl
from itertools import product
"""
Chapter 10. Network Models. Transportation.
Anderson, David R., Dennis J. Sweeney,
Thomas A. Williams,
Jeffrey D. Camm y Kipp Martin
Quantitative Methods for Business, 11a. Ed
"""

loads = {
    'Cleveland':  5_000, 
    'Bedford':    6_000,
    'York':       2_500,
    'Boston':    -6_000,
    'Chicago':   -4_000,
    'St. Louis': -2_000,
    'Lexington': -1_500,
}
a = [
    [0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    ]

costs = [
   [1_000,  1_000, 1_000, 3, 2, 7, 6],
   [1_000,  1_000, 1_000, 7, 5, 2, 3],
   [1_000,  1_000, 1_000, 2, 5, 4, 5],
   [1_000,  1_000, 1_000, 1_000, 1_000, 1_000, 1_000],
   [1_000,  1_000, 1_000, 1_000, 1_000, 1_000, 1_000],
   [1_000,  1_000, 1_000, 1_000, 1_000, 1_000, 1_000],
   [1_000,  1_000, 1_000, 1_000, 1_000, 1_000, 1_000],
    ]


a = pl.makeDict((loads, loads), a, 0)
costs = pl.makeDict((loads, loads), costs, 0)


# problem
problem = pl.LpProblem('Transportation', pl.LpMinimize)

# arcs
# routes = [*product(sources, sinks)]

# variables
transport = pl.LpVariable.dicts('Route', (loads, loads), 0, None, pl.LpContinuous)
# print('\n', transport)

# objective function
problem += pl.lpSum(costs[source][sink] * transport[source][sink] for source in loads for sink in loads), 'Sum_Transporting_Costs'

# Supply Constraints
for k, v in loads.items():
    problem += pl.lpSum(transport[k][out] for out in loads ) - pl.lpSum(transport[enter][k] for enter in loads ) == v, f'num_products_out_{k}'


solver = pl.get_solver('GUROBI') 
problem.solve(solver)

# The status of the solution is printed to the screen
print("Status:", pl.LpStatus[problem.status])


# Each of the variables is printed with it's resolved optimum value
for v in problem.variables():
    if v.varValue > 1e-10:
        print(f'{v.name}: {v.varValue:,.2f}')

# The optimised objective function value is printed to the screen
print(f'Total Cost of Transportation = {pl.value(problem.objective):,.2f}')
