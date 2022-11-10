import pulp as pl
from itertools import product
"""
Chapter 10. Network Models. Assignment.
Anderson, David R., Dennis J. Sweeney,
Thomas A. Williams,
Jeffrey D. Camm y Kipp Martin
Quantitative Methods for Business, 11a. Ed
"""

sources = {
    'Terry': 1, 
    'Carle': 1,
    'McClymonds': 1,
}

sinks = {
    'Customer01': 1,
    'Customer02': 1,
    'Customer03': 1,
}

costs =  [
    [10, 15, 9],
    [9, 18, 5],
    [6, 14, 3],
]


costs = pl.makeDict((sources, sinks), costs, 0)


# problem
problem = pl.LpProblem('Transportation', pl.LpMinimize)

# arcs
routes = [*product(sources, sinks)]

# variables
vars = pl.LpVariable.dicts('Assignment', (sources, sinks), 0, None, pl.LpContinuous)
# print('\n', vars)

# objective function
problem += pl.lpSum(costs[source][sink] * vars[source][sink] for source in sources for sink in sinks), 'Sum_Of_Days'

# Supply Constraints
for source, supply in sources.items():
    problem += pl.lpSum(vars[source][sink] for sink in sinks ) <= supply, f'num_assignment_out_{source}'

# Demand Constraint
for sink, demand in sinks.items():
    problem += pl.lpSum(vars[source][sink] for source in sources) == demand, f'num_assignment_into_{sink}'

solver = pl.get_solver('GUROBI') 
problem.solve(solver)

# The status of the solution is printed to the screen
print("Status:", pl.LpStatus[problem.status])


# Each of the variables is printed with it's resolved optimum value
for v in problem.variables():
    if v.varValue > 1e-10:
        print(f'{v.name}: {v.varValue:,.2f}')

# The optimised objective function value is printed to the screen
print(f'Total Days = {pl.value(problem.objective):,.2f}')
