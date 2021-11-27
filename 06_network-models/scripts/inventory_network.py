#%%
import gurobipy as gp
from gurobipy import GRB


# %% [markdown]
# # Parameters
# %%

arcs, costs = gp.multidict({
    ('prod01', 'demand01'): 2,
    ('prod02', 'demand02'): 5,
    ('prod03', 'demand03'): 3,
    ('prod04', 'demand04'): 3,
    ('demand01', 'demand02'): 0.25,
    ('demand02', 'demand03'): 0.25,
    ('demand03', 'demand04'): 0.25,
})


supply = {
    'prod01': 600,
    'prod02': 300,
    'prod03': 500,
    'prod04': 400,
}

demand = {
    'demand01': 400,
    'demand02': 500,
    'demand03': 400,
    'demand04': 400,
}

#%% [markdown]
## Model
### Decision Variables
#%%
m = gp.Model('inventory')
yards = m.addVars(arcs, vtype=GRB.CONTINUOUS, name='yards')
#%% [markdown]
### Objective Function
#%%
Z = yards.prod(costs)
m.ModelSense = GRB.MINIMIZE
m.setObjective(Z)

#%% [markdown]
### Constraints
#%%
source = m.addConstrs(
    (yards.sum(i, '*') <= s for i,s in supply.items()),
    name='source'
)

transshipment = m.addConstrs(
    # In - Out = Demand   <--> In = Demand + Out
    (yards.sum('*', t) - yards.sum(t, '*')  == d for t,d in demand.items() ),
    name='inventory'
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
print(f'Minimum Cost ${m.ObjVal:,.2f} \n')

for v in m.getVars():
    if abs(v.X) > 0.000001:
        print(f'{v.VarName}: {v.X}')

