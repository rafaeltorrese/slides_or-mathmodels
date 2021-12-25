#%%
import gurobipy as gp
from gurobipy import GRB

#%% [markdown]
### Parameters
#%%
arcs, capacity = gp.multidict({
    (1, 2): 5,
    (1, 3): 6,
    (1, 4): 5,
    #
    (2, 3): 2,
    (2, 5): 3,
    #
    (3, 2): 2,
    (3, 4): 3,
    (3, 5): 3,
    (3, 6): 7,
    #
    (4, 6): 5,
    #
    (5, 6): 1,
    (5, 7): 8,
    #
    (6, 5): 1,
    (6, 7): 7,
    #
    (7, 1): GRB.INFINITY,
})


#%%
nodes = range(1, 8)
#%% [markdown]
## Model
### Decision Variables
#%%
m = gp.Model('max_flow')
path = m.addVars(arcs, ub=capacity, vtype=GRB.CONTINUOUS, name='path')
#%% [markdown]
### Objective Function
#%%
Z = path[7,1]
m.ModelSense = GRB.MAXIMIZE
m.setObjective(Z)
#%% [markdown]
### Constraints
#%% 
transshipment = m.addConstrs(
    (path.sum('*', t) - path.sum(t, '*') == 0 for t in nodes),
    name='transshipment'
)

# %%
m.update()
print(f'Number of variables: {m.NumVars}')
print(f'Number of constraints: {m.NumConstrs}')
print(f'Constraints are \n {m.getConstrs()}')
#%% [markdown]
### Optimization process
# %%
m.optimize()
#%% [markdown]
### Results
#%%
print(f'Max Flow: {m.objVal * 1000:,.0f} vehicles')
#%%
for v in m.getVars():
    if abs(v.x) > 1e-5:
        print(f'{v.VarName}: {v.x * 1000:,.0f}')
# %%
