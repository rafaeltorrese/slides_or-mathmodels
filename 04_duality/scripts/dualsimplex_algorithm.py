import numpy as np

def dual_simplex(matrix, rhs, z, numxvars):
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
    matrix = np.array(matrix)
    rhs = np.array(rhs)
    z = np.array(z)

    num_rows, num_cols = matrix.shape

    onecols = np.where(matrix == 1)[1]
    cb_index = onecols[onecols >= numxvars]
    cb = z[cb_index]

    zj = cb.dot(matrix)

    net_evaluation = z - zj

    solutions = []
    fvalues = []

    iteration = 0
    if np.any(net_evaluation > 0):
            print("Method Fails")
            print("Net Evaluation Row", net_evaluation)
    while np.all(net_evaluation <= 0) and np.any(rhs < 0) :
        solution = np.zeros_like(z)

        leaving = rhs.argmin()   # leaving variables (index)
        key_row = matrix[leaving]

        if np.all(key_row>=0):
            print("Infeasible Solution")
            break

        ratios = np.divide(net_evaluation, key_row, out=np.full_like(z, np.inf), where=key_row<0)

        entering = ratios.argmin()

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
        net_evaluation = z - zj

        solution[cb_index] = rhs  # basics

        iteration += 1

        print(f"Iteration {iteration}")
        print(matrix,  "\n")
        print("Solution", solution, f"\tZ: {cb.dot(rhs):0.2f}", "\n")

        solutions.append(solution)
        fvalues.append(cb.dot(rhs))
        if np.any(net_evaluation > 0):
            print("Method Fails")
            break

        if np.all(net_evaluation <= 0) and np.all(rhs >= 0):
            print(f"Optimal solution found in {iteration} iterations")

    return np.array(solutions), fvalues, np.vstack((zj, net_evaluation))

if __name__ == '__main__':
    pass