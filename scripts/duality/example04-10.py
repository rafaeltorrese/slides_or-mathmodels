"""
Example 10
  A feed mixing operation can be described in terms of the two activities. The required mixture must contain four kinds of ingredients $w, x, y$ and $z$. Two basic feeds $A$ and $B$, which contain the required ingredients are available in the market. One kg. of $A$ contains 0.1 kg. of $w$, 0.1 kg. of $y$ and 0.2 kg. of $z$. Likewise, one kg. of feed $B$ contains 0.1 kg. of $x$, 0.2 kg. of $y$,  and 0.1 kg. of $z$. The daily per head requirement is of at least 0.4 kg. of $w$, 0.6 kg. of $x$, 2 kg. of $y$ and 1.8 kg. of $z$. Feed $A$ can be bought for \$0.07 per kg. and $B$ can be bought for \$ 0.05 per kg. The availabilities, requirements and costs are summarized in the following table.


\min Z = 0.07x_1 + 0.05x_2

01x_1  \geq 0.4
0.1x_2 \geq 0.6
0.1x_1 + 0.2x_2 \geq 2.0
0.2x_1 + 0.1x_2 \geq 1.8

"""
from pprint import pprint
import numpy as np
from algorithms import simplex, twophase, analytical

np.set_printoptions(precision=3, suppress=True)
#%% Primal Problem
I = np.diag([-1,-1, -1,-1])
A = np.diag([1, 1, 1, 1])

cj = np.array(np.concatenate(([0.07, 0.05, 0, 0, 0, 0], 1000 * np.diag(A))), dtype=float)

body = np.array([
    [0.1, 0.0],
    [0.0, 0.1],
    [0.1, 0.2],
    [0.2, 0.1],
], dtype=float)

M = np.concatenate((body, I, A), axis=1)
b = np.array([0.4, 0.6, 2.0, 1.8], dtype=float)

solutions_primal, zvalues, lastrow_primal = simplex(matrix=M, rhs=b, z=cj, numxvars=2, direction=-1)

#%%

M2 = np.concatenate((body.T, np.diag([1,1])), axis=1)
print(M2)

c2j = np.concatenate((b, np.full(M2.shape[0], 0)))

b2 = cj[ : M2.shape[0] ]


solution_dual, wvalues, lastrow_dual = simplex(matrix=M2, rhs=b2, z=c2j, numxvars=4, direction=1)


print()
print(lastrow_primal[:, :-2])
print()
print(solution_dual[-1])