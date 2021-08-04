import numpy as np

def simplex_revised(matrix, rhs, z, numxvars, direction=1):
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
        Use +1 for maximization and -1 for minimization.

    Returns
    -------
    solutions: numpy ndarray
        Vector solutions of every iteration

    fvalues: numpy ndarray
        Values of z (objective function)

    lastrows: numpy ndarray
        Last rows of optimal table, this rows corresponde to Zj and cj - Zj
    '''
    print("======= Simplex Revised Method ======= ")

    matrix = np.array(matrix, dtype=float)
    rhs = np.array(rhs, dtype=float)
    z = np.array(z, dtype=float)

    num_rows, num_cols = matrix.shape

    onecols = np.where(matrix == 1)[1]
    cb_index = onecols[onecols >= numxvars]
    cb = z[cb_index]

    Bmatrix = matrix[:, cb_index]
    Binv = np.linalg.inv(Bmatrix)
    pimult = cb.dot(Binv)

    zj = pimult.dot(matrix)
    net_evaluation = direction * (z - zj)

    solutions = []
    fvalues = []

    labels = [f"x{i + 1}" for i in range(num_cols)]

    iteration = 0

    while np.any(net_evaluation > 1e-08):
        solution = np.zeros_like(z)

        entering = net_evaluation.argmax()
        entering_label = labels[entering]

        P = matrix[:, entering]
        pivot_column = Binv.dot(P)

        ratios = np.divide(rhs, pivot_column,
                           out=np.full_like(rhs, np.inf),
                           where=pivot_column > 0)

        leaving = ratios.argmin()
        leaving_label = labels[cb_index[leaving]]

        pivot = pivot_column[leaving]

        if pivot != 1:
            pivot_column[leaving] /= pivot
            rhs[leaving] /= pivot
            Binv[leaving] /= pivot

        for i in range(num_rows):
            if i != leaving:
                factor = pivot_column[i]
                pivot_column[i] += -factor * pivot_column[leaving]
                Binv[i] += -factor * Binv[leaving]
                rhs[i] += -factor * rhs[leaving]

        cb_index[leaving] = entering
        cb = z[cb_index]
        pimult = cb.dot(Binv)

        zj = pimult.dot(matrix)

        net_evaluation = direction * (z - zj)

        solution[cb_index] = rhs  # basics

        iteration += 1

        solutions.append(solution)
        fvalues.append(cb.dot(rhs))

        print(f"Iteration {iteration}. {leaving_label} ---> {entering_label}")
        # print(Binv.dot(matrix),  "\n")
        print("Solution", solution, f"\tZ: {cb.dot(rhs):0.2f}", "\n")

        if np.all(net_evaluation <= 1e-08):
            print(f"Optimal solution found in {iteration} iterations")
            print((*zip(labels, np.round(solution, 3))))

    return np.array(solutions), fvalues, np.vstack((zj, net_evaluation))
