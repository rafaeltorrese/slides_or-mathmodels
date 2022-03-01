import numpy as np 

def simplex(A, rhs, cj, direction=1, cbidx=None):
    A = A.astype(float)
    rhs = rhs.astype(float)
    cj = cj.astype(float)

    num_equations, num_variables = A.shape
    
    if cbidx:
        cb_index = cbidx
    else:
        cb_index = np.nonzero((np.abs(A).sum(axis=0) == 1) & (A.sum(axis=0) == 1) )[0]    
    cb = cj[cb_index]
    
    print(f'Cb index {cb_index}')
    print(f'Cb: {cb}')
    zj = cb.dot(A)    
    net_profit = direction * (cj - zj)

    iteration = 0
    basis = []
    row_index = [*range(num_equations)]
    labels = [f'x_{i}' for i in range(1, num_variables + 1)]
    while np.any(net_profit > 0):
        ratios = np.full(num_equations, np.inf)

        entering_idx = net_profit.argmax()
        key_column = A[:, entering_idx]
        np.divide(rhs, key_column, out=ratios, where=key_column > 0)

        leaving_idx = ratios.argmin()

        pivot = A[leaving_idx, entering_idx]
        print(f'Leaving {labels[cb_index[leaving_idx]]}. Entering {labels[entering_idx]}')

        if pivot != 1:
            A[leaving_idx] /=  pivot
            rhs[leaving_idx] /=  pivot
        
    
        rows_index = [*range(num_equations)]
        rows_index.remove(leaving_idx)
        for i in rows_index:
            target  = -A[i, entering_idx]
            A[i] += target * A[leaving_idx]
            rhs[i] += target * rhs[leaving_idx]


        cb_index[leaving_idx] = entering_idx
        cb = cj[cb_index]
        zj = cb.dot(A)    
        net_profit = direction * (cj - zj)
        iteration += 1
        basis.extend(cb_index)
        print(f'Zvalue: {cj[cb_index].dot(rhs)}')
    
    
    print(f'Total iterations {len(np.array(basis).reshape((-1, num_equations)))}')
    return np.array(basis).reshape((-1, num_equations)).tolist(), A, rhs