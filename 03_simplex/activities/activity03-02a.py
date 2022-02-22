#%%
from itertools import combinations
import numpy as np
from pprint import pprint
#%%
def labels_combination(variables, nrows):
    return (tuple(combinations(variables, nrows)))

#%%
A = np.array(
    [
        [1, 1, 1, 0, 0, 0, 0],
        [0, 1, 0, -1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0],
        [1, -1, 0, 0, 0, -1, 0],
        [1, 0, 0, 0, 0, 0, 1],
        ]
)

b = np.array(
    [30,
    3,
    12,
    0,
    20,]
)

z = np.array(
    [
        2,
        3,
        0,
        0,
        0,
        0,
        0,
    ]
)
#%%
labels = np.array('x1 x2 s1 s2 s3 s4 s5'.split())
print(labels)
#%%
m, n = A.shape
comb_list = tuple(combinations(range(n), m))
total_combinations = len(comb_list)
print(f'Number of equations: {m}')
print(f'Number of variables: {n}')
print(f'Number of combinations: {total_combinations}')
#%%
# pprint(comb_list)
comblabs = labels_combination(variables=labels, nrows=m)
np.savetxt(fname='./03_simplex/activities/combinations03-02a.csv', X=comblabs,  header='x1 x2 s1 s2 s3 s4 s5', delimiter=',', fmt='%s')
# pprint(np.array(comblabs))

