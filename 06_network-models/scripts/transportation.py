#%%
import gurobipy as gp
from gurobipy import GRB

#%% [markdown]
# # Parameters
#%%
arcs, costs = gp.multidict({
    ('Cleveland','Boston'): 3, 
    ('Cleveland','Chicago'): 2,
    ('Cleveland','StLouis') :7,
    ('Cleveland','Lexington'): 6,
    ('Bedford','Boston'): 7,
    ('Bedford','Chicago'): 5,
    ('Bedford','StLouis'): 2,
    ('Bedford','Lexington'): 3,
    ('York', 'Boston'): 2,
    ('York', 'Chicago'): 5,
    ('York', 'StLouis'): 4,
    ('York', 'Lexington'): 5,
})


supply = {
    'Cleveland': 5_000,
    'Bedford':  6_000,
    'York': 2_500,
}

demand = {
    'Boston': 6_000,
    'Chicago': 4_000,
    'StLouis': 2_000,
    'Lexington': 1_500,
}


#%% [markdown]
## Model
### Decision Variables
#%%
m = gp.Model('transportation')
send = m.addVars(arcs,  vtype=GRB.CONTINUOUS, name='send')

#%% [markdown]
# # Objective Function
#%%
Z = send.prod(costs)
m.ModelSense = GRB.MINIMIZE
m.setObjective(Z)

# %% [markdown]
# # Constraints
# %%
source = m.addConstrs(
    (send.sum(i, '*') <= s for i,s in supply.items() ),
    name='source'
)

sink = m.addConstrs(
    (send.sum('*', j) == d for j,d in demand.items()),
    name='sink'
)
# %%
m.update()
print(f'Number of constraints {m.NumConstrs}')
print(f'Number of variables {m.NumVars}')
print(f'Constraints are \n {m.getConstrs()} \n')
#%% [markdown]
### Optimization process
# %%
m.optimize()

#%% [markdown]
### Results
#%%
print(f'Objective value: ${m.objVal:,.2f}\n')
#%%
for v in m.getVars():
    if abs(v.X) > 0.00001:
        print(f'{v.VarName}: {v.x:,.0f}') 
