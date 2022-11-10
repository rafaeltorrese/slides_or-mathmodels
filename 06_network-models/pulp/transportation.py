import pulp as pl
from itertools import product
"""
Chapter 10. Network Models. Transportation.
Anderson, David R., Dennis J. Sweeney,
Thomas A. Williams,
Jeffrey D. Camm y Kipp Martin
Quantitative Methods for Business, 11a. Ed
"""

sources = {
    'Cleveland': 5_000, 
    'Bedford': 6_000,
    'York': 2_500,
}

sinks = {
    'Boston': 6_000,
    'Chicago': 4_000,
    'St. Louis': 2_000,
    'Lexington': 1_500,
}

costs =  [
    [3, 2, 7, 6],
    [7, 5, 2, 3],
    [2, 5, 4, 5],
]


costs = pl.makeDict((sources, sinks), costs, 0)


# problem
problem = pl.LpProblem('Transportation', pl.LpMinimize)

# arcs
routes = [*product(sources, sinks)]

# variables
vars = pl.LpVariable.dicts('Route', (sources, sinks), 0, None, pl.LpContinuous)
# print('\n', vars)

# objective function
problem += pl.lpSum(costs[source][sink] * vars[source][sink] for source in sources for sink in sinks), 'Sum_Transporting_Costs'

# Supply Constraints
for source, supply in sources.items():
    problem += pl.lpSum(vars[source][sink] for sink in sinks ) <= supply, f'num_products_out_{source}'

# Demand Constraint
for sink, demand in sinks.items():
    problem += pl.lpSum(vars[source][sink] for source in sources) == demand, f'num_products_into_{sink}'

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
