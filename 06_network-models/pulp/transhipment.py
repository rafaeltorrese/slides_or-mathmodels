"""
Chapter 10. Network Models. Transhipment.
Anderson, David R., Dennis J. Sweeney,
Thomas A. Williams,
Jeffrey D. Camm y Kipp Martin
Quantitative Methods for Business, 11a. Ed
"""
from itertools import product
import math

import pulp as pl



sources = {
    'Denver': 600, 
    'Atlanta': 400,
    'Kansas': math.inf,
    'Louisville': math.inf,
}

transhipments = {
    'Kansas': 0,
    'Louisville': 0,
}

sinks = {
    'Kansas': 0,
    'Louisville': 0,
    'Detroit': 200,
    'Miami': 150,
    'Dallas': 350,
    'New Orleans': 300,
}

costs =  [
    [2, 3, 1_000_000,1_000_000,1_000_000,1_000_000 ],
    [3, 1, 1_000_000,1_000_000,1_000_000,1_000_000 ],
    [1_000_000, 1_000_000,  2, 6, 3, 6],
    [1_000_000, 1_000_000,  4, 4, 6, 5],
]


costs = pl.makeDict((sources, sinks), costs, 0)


# problem
problem = pl.LpProblem('Transhipment', pl.LpMinimize)

# arcs
routes = [*product(sources, sinks)]

# variables
send = pl.LpVariable.dicts('Send', (sources, sinks), 0, None, pl.LpContinuous)
# print('\n', vars)

# objective function
problem += pl.lpSum(costs[source][sink] * send[source][sink] for source in sources for sink in sinks), 'Sum_Costs_Transportation'

# Supply Constraints
for source, supply in sources.items():
    problem += pl.lpSum(send[source][sink] for sink in sinks ) <= supply, f'num_product_out_{source}'

# Transhipment Constraints
for city, demand in transhipments.items():
    problem += pl.lpSum(send[source][city] for source in sources) - pl.lpSum(send[city][sink] for sink in sinks) == demand, f'num_transhipment_into_{city}'

# Demand Constraints
for sink, demand in sinks.items():
    problem += pl.lpSum(send[source][sink] for source in sources) >= demand, f'num_products_into_{sink}'

solver = pl.get_solver('GUROBI') 
problem.solve(solver)

# The status of the solution is printed to the screen
print("Status:", pl.LpStatus[problem.status])


# Each of the variables is printed with it's resolved optimum value
for v in problem.variables():
    if v.varValue > 1e-10:
        print(f'{v.name}: {v.varValue:,.2f}')

print(f'Total Cost of Transportation = {pl.value(problem.objective):,.2f}')
