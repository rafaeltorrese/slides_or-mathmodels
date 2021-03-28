import numpy as np

def phase1(matrix, rhs, z, numxvars):
    '''Simplex algorithm to solve linear programming problems

    Parameters
    ----------
    matrix: numpy ndarray
        Matrix of coefficients in the left-hand side

    rhs: numpy ndarray
        Right-hand side vector

    numxvars: int
        Number of x variables

    direction: {+1 , -1}
        For maximization problems use +1 and for minimization problems use -1 instead.
    '''
    print("="*30, "PHASE I", "="*30, "\n")


    num_rows, num_cols = matrix.shape
    onecols = np.where(matrix == 1)[1]
    cb_index = onecols[onecols >= numxvars]

    w = np.where(np.abs(z) >= 1000 , 1, 0)  # new objective function
    cb = w[cb_index]
    zj = cb.dot(matrix)
    net_evaluation = zj - w

    solutions = []
    zvalues = []

    iteration = 0
    status = True
    while np.any(net_evaluation > 0):
        solution = np.zeros_like(z)
        entering = net_evaluation.argmax()  # entering variables (index)

        key_col = matrix[ : , entering]
        ratios = np.divide(rhs, key_col, out=np.full_like(rhs, np.inf), where=key_col>0)
        leaving = ratios.argmin()   # leaving variables (index)
        pivot = matrix[leaving, entering]

        if pivot != 1:
            matrix[leaving] = matrix[leaving] / pivot
            rhs[leaving] = rhs[leaving] / pivot

        for i in range(num_rows):
            if i == leaving:
                continue
            factor = matrix[i, entering]
            matrix[i] = -factor * matrix[leaving] + matrix[i]
            rhs[i] = -factor * rhs[leaving] + rhs[i]

        cb_index[leaving] = entering
        cb = w[cb_index]

        zj = cb.dot(matrix)

        net_evaluation = zj - w

        solution[cb_index] = rhs  # basics

        iteration += 1
        print(f"Iteration {iteration}")
        print(matrix,  "\n")
        print("Solution", solution, f"\tZ: {cb.dot(rhs):0.2f}", "\n")

        zvalues.append(cb.dot(rhs))
        solutions.append(solution)

    if cb.dot(rhs) > 0:
        status = False  # non-optimal
    return cb_index, solutions, zvalues, iteration, status


def phase2(matrix, rhs, z, numxvars, cb_index, solutions, zvalues, iteration, direction):
# def phase2(z, direction=1):
    '''Simplex algorithm to solve linear programming problems

    Parameters
    ----------
    matrix: numpy ndarray
        Matrix of coefficients in the left-hand side

    rhs: numpy ndarray
        Right-hand side vector

    numxvars: int
        Number of x variables

    direction: {+1 , -1}
        For maximization problems use +1 and for minimization problems use -1 instead.
    '''
    print("="*30, "PHASE II", "="*30, "\n")

    num_rows = len(matrix)

    cb = z[cb_index]
    zj = cb.dot(matrix)

    net_evaluation = direction * (z - zj)

    solution = np.zeros_like(z)
    solution[cb_index] = rhs

    zvalues[-1] = cb.dot(rhs)
    if np.all(net_evaluation <= 0):
            print(solution, cb.dot(rhs), "\n")
            print(f"Optimal solution found in {iteration} iterations" )

    while np.any(net_evaluation > 0):
        solution = np.zeros_like(z)
        entering = net_evaluation.argmax()  # entering variables (index)

        key_col = matrix[ : , entering]
        ratios = np.divide(rhs, key_col, out=np.full_like(rhs, np.inf), where=key_col>0)
        leaving = ratios.argmin()   # leaving variables (index)
        pivot = matrix[leaving, entering]

        if pivot != 1:
            matrix[leaving] = matrix[leaving] / pivot
            rhs[leaving] = rhs[leaving] / pivot

        for i in range(num_rows):
            if i == leaving:
                continue
            factor = matrix[i, entering]
            matrix[i] = -factor * matrix[leaving] + matrix[i]
            rhs[i] = -factor * rhs[leaving] + rhs[i]

        cb_index[leaving] = entering
        cb = z[cb_index]

        zj = cb.dot(matrix)

        net_evaluation = direction * (z - zj)

        solution[cb_index] = rhs  # basics

        iteration += 1
        print(f"Iteration {iteration}")
        print(matrix,  "\n")
        zvalues.append(cb.dot(rhs))
        print("Solution", solution, f"\tZ: {cb.dot(rhs):0.2f}", "\n")

        solutions.append(solution)
        if np.all(net_evaluation <= 0):
            print(f"Optimal solution found in {iteration} iterations")
    return np.array(solutions), zvalues

def twophase(matrix, rhs, z, numxvars, direction=1):
    '''Simplex algorithm to solve linear programming problems

    Parameters
    ----------
    matrix: numpy ndarray
        Matrix of coefficients in the left-hand side

    rhs: numpy ndarray
        Right-hand side vector

    numxvars: int
        Number of x variables

    direction: {+1 , -1}
        For maximization problems use +1 and for minimization problems use -1 instead.
    '''
    cbind, sols, values, itr, is_optimal = phase1(matrix, rhs, z, numxvars)
    if is_optimal:
        return phase2(matrix, rhs,  z, numxvars, cb_index=cbind, solutions=sols, zvalues=values, iteration=itr, direction=direction)
    else:
        print("INFEASIBLE")
