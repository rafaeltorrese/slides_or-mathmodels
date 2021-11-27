#%%
from pprint import pprint
import gurobipy as gp
from gurobipy import GRB

#%% [markdown]
## Parameters
#%%
arcs, days = gp.multidict({
    ('Terry', 'Customer01'): 10,
    ('Terry', 'Customer02'): 15,
    ('Terry', 'Customer03'):  9,
    #
    ('Carle', 'Customer01'):  9,
    ('Carle', 'Customer02'): 18,
    ('Carle', 'Customer03'):  5,
    #
    ('McClymonds', 'Customer01'):  6,
    ('McClymonds', 'Customer02'): 14,
    ('McClymonds', 'Customer03'):  3,
})

supply = {
    'Terry': 1,
    'Carle':  1,
    'McClymonds': 1,
}

demand = {
    'Customer01': 1,
    'Customer02': 1,
    'Customer03': 1,
}

#%% [markdown]
## Model
### Decision Variables
#%%

m = gp.Model('assignment')
assign = m.addVars(arcs, vtype=GRB.CONTINUOUS, name='assign')
#%% [markdown]
### Objective Function
#%%
Z = assign.prod(days)
m.ModelSense = GRB.MINIMIZE 
m.setObjective(Z)
#%% [markdown]
### Constraints
#%%
source = m.addConstrs(
    (assign.sum(i,'*') <= s for  i,s in supply.items()),
    name='leaders'
)

sink = m.addConstrs(
    (assign.sum('*', j) == d for j,d in demand.items()),
    name='customers'
)
#%%
m.update()
print(f'Number of constraints {m.NumConstrs}')
print(f'Number of variables {m.NumVars}')
print('Constraints are')
pprint(m.getConstrs())
#%% [markdown]
### Optimization process
# %%
m.optimize()

#%% [markdown]
### Results
#%%
print(f'Objective Value {m.objVal} days')

for v in m.getVars():
    if abs(v.X) > 0.00001:
        print(f'{v.VarName}: {v.X}')
