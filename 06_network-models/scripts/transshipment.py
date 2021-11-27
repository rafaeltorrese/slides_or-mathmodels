#%%
import gurobipy as gp
from gurobipy import GRB

#%% [markdown]
### Parameters
#%%

arcs, costs = gp.multidict({
    ('Denver', 'Kansas'): 2,
    ('Denver', 'Louisville'): 3,
    #
    ('Atlanta', 'Kansas'): 3,
    ('Atlanta', 'Louisville'): 1,
    #
    ('Kansas', 'Detroit'): 2,
    ('Kansas', 'Miami'): 6,
    ('Kansas', 'Dallas'): 3,
    ('Kansas', 'NewOrleans'): 6,
    #
    ('Louisville', 'Detroit'): 4,
    ('Louisville', 'Miami'): 4,
    ('Louisville', 'Dallas'): 6,
    ('Louisville', 'NewOrleans'): 5,
})

supply = {
    'Denver': 600,
    'Atlanta': 400,

}

demand = {
    'Kansas': 0, 
    'Louisville':0,
    'Detroit': 200,
    'Miami': 150,
    'Dallas':350, 
    'NewOrleans': 300,
}

#%% [markdown]
## Model
### Decision Variables
#%%

m = gp.Model('transshipment')
send = m.addVars(arcs, vtype=GRB.CONTINUOUS, name='send')
#%% [markdown]
### Objective Function
#%%
Z = send.prod(costs)
m.ModelSense = GRB.MINIMIZE
m.setObjective(Z)

#%% [markdown]
### Constraints
#%% 
source = m.addConstrs(
    (send.sum(i,'*') <= s for i,s in supply.items()),
    name='source'
)

sinks = m.addConstrs(
    # Out - In = - D  <--> In - Out = D
    (send.sum('*',k) - send.sum(k, '*')  == d for k,d in demand.items()),
    name='sinks'
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
print(f'Objective value ${m.objVal:,.2f}')

for v in m.getVars():
    if abs(v.X) > 0.000001:
        print(f'{v.VarName}: {v.X}')
