#%%
import gurobipy as gp
from gurobipy import GRB
#%% [markdown]
### Parameters
#%%
arcs, distances = gp.multidict({
    (1, 2): 25,
    (1, 3): 20,
    #
    (2, 3):  3,
    (2, 4):  5,
    (2, 6): 14,
    #
    (3, 2):  3,
    (3, 5):  6,
    #
    (4, 2):  5,
    (4, 5):  4,
    (4, 6):  4,
    #
    (5, 3):  6,
    (5, 4):  4,
    (5, 6):  7,
})

supply = {
    1:1,
}

demand = {
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 1,
}

#%% [markdown]
## Model
### Decision Variables
#%%
m = gp.Model('shortest_path')
path = m.addVars(arcs, vtype=GRB.CONTINUOUS, name='path')
#%% [markdown]
### Objective Function
#%%
Z = path.prod(distances)
m.ModelSense = GRB.MINIMIZE
m.setObjective(Z)
#%% [markdown]
### Constraints
#%% 
source = m.addConstrs(
    (path.sum(i,'*') <= s for i,s in supply.items()),
    name='source'
)

sink = m.addConstrs(
    (path.sum('*', j) - path.sum(j, '*') == d for j,d in demand.items()),
    name='sink'
)
# %%
m.update()
print(f'Number of variables: {m.NumVars}')
print(f'Number of constraints: {m.NumConstrs}')
print(f'Constraints are \n {m.getConstrs()} \n')
#%% [markdown]
### Optimization process
# %%
m.optimize()

#%% [markdown]
### Results
#%%
print(f'Minimum distance: {m.objVal} miles')

for v in m.getVars():
    if abs(v.X) > 0.00001:
        print(f'{v.VarName}: {v.x}')