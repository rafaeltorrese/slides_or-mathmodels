from itertools import combinations
import numpy as np


def create_fullmatrix(body, inequalities, c, varlabel="x", direction=1, M=1000 ):
    """
    This function creates body matrix to solve a Linear Programming Problem through Simplex Method


    Parameters
    -----------

    body: numpy ndarray
        Left-hand side of the problem

    inequalities: list of strings
        Inequalities in each constraint

    c: list of floats
        Coefficients in the objective function

    varlabel: string, default="x"
        Letter for identify the main variable in the problem, for example x1, x2, xn or y1, y2, ..., yn

    direction: {-1, +1}
        Sense of the problem. -1 for minimization problems or +1 for maximization problems

    M: int, default=1000
        If there are artificial variables, maybe the method for solving is BigM method, so, we need to set a penalty where M represents a big number.
    """
    if not isinstance(body, np.ndarray):
        body = np.array(body, dtype=float)
    if not isinstance(c, np.ndarray):
        c = np.array(c, dtype=float)
    rows, cols = body.shape
    labels = []
    signs = []
    row_positions = []
    zaux = []
    for i, ineq in enumerate(inequalities):
        if ineq == "<=":
            labels += [f"s{i + 1}"]
            signs += [1]
            row_positions += [i]
            zaux += [0]
        elif ineq == ">=":
            labels += [f"s{i + 1}", f"A{i + 1}" ]
            signs += [-1, 1]
            row_positions += [i, i]
            zaux += [0, M]
        else:
            labels += [f"A{i + 1}"]
            signs += [1]
            row_positions += [i]
            zaux += [M]

    samatrix = np.zeros((rows, len(labels)))  # slack artificial matrix
    samatrix[row_positions, range(len(labels))] = signs
    full_labels = [f"{varlabel}{i + 1}" for i in range(cols)] + labels
    full_matrix = np.hstack((body, samatrix))

    cj = np.concatenate((c, direction * -np.array(zaux)))
    return full_matrix, full_labels, cj


def simplex(matrix, rhs, z, inequalities, direction=1, M=1000, vlabel="x"):
    '''Simplex algorithm to solve linear programming problems

    Parameters
    ----------
    matrix: numpy ndarray
        Matrix of coefficients in the left-hand side

    rhs: numpy ndarray
        Right-hand side vector

    inequalities: list of strings
        List with inequality strings

    M: int, default=1000
       Penalty quantity

    direction: {+1 , -1}
        For maximization problems use +1 and for minimization problems use -1 instead.
    '''
    print("=" * 20, "Simplex Method", "=" * 20)
    if not isinstance(matrix, np.ndarray):
        matrix = np.array(matrix, dtype=float)

    numconstraints, numxvars = matrix.shape
    rhs = np.array(rhs, dtype=float)

    matrix, labels, z = create_fullmatrix(matrix, inequalities, z, vlabel, direction, M)

    # num_rows, num_cols = matrix.shape
    
    cb_index = np.where((matrix == 1) & (np.abs(matrix).sum(axis=0) == 1))[1]

    cb = z[cb_index]

    zj = cb.dot(matrix)

    net_evaluation = direction * (z - zj)

    solutions = []
    fvalues = []

    iteration = 0
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

        for i in range(numconstraints):
            if i == leaving:
                continue
            factor = matrix[i, entering]
            matrix[i] = -factor * matrix[leaving] + matrix[i]
            rhs[i] = -factor * rhs[leaving] + rhs[i]

        leaving_label = labels[cb_index[leaving]]
        entering_label= labels[entering]

        cb_index[leaving] = entering

        cb = z[cb_index]
        zj = cb.dot(matrix)
        net_evaluation = direction * (z - zj)

        solution[cb_index] = rhs  # basics

        iteration += 1


        print(f"Iteration {iteration}. Entering: {entering_label}, Leaving: Leaving: {leaving_label}")
        print(matrix,  "\n")
        print("Solution", solution, f"\tZ: {cb.dot(rhs):0.2f}", "\n")

        solutions.append(solution)
        fvalues.append(cb.dot(rhs))
        if np.all(net_evaluation <= 0):
            print(f"Optimal solution found in {iteration} iterations")
            print((*zip(labels, np.round(solution, 4))))
    return np.array(solutions), fvalues, np.vstack((zj, net_evaluation))





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
    matrix = np.array(matrix)
    rhs = np.array(rhs)
    z = np.array(z)

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

def analytical(matrix, rhs, objcoef, constant=0, direction="max"):
    '''Analytical method to solve a linear programming problem

    This function solves linear programming problems through trial and error method (analytical method). This method uses a greedy approch by solving all linear equation subsystems. The total number of basic solutions are the combinations of m equations in m+n variables, where m + n variables are the total number of variables whenever the standard form for linear programs are used.

    Parameters
    ----------
    matrix: numpy.ndarray
       Body matrix of the linear programming problem (left-hand side)

    rhs: numpy.ndarray
        The right-hand side of the linear programming problem

    objcoef: numpy.ndarray
        Objective function coefficients in the standard form. The zeros corresponding to slack or surplus variables must be taken into account.

    constant: scalar, default 0
        If the objective function has an independent term, this one must be included as part of the objective function.

    direction: {"max", "min"}
        Sense of the objective function (the default is "max", which implies a maximization problem)

    Returns
    ----------
    feasible_solutions: numpy ndarray
        Matrix with feasible solutions

    infeasible_solutions: numpy ndarray
        Matrix with infeasible solutions

    best_vector: numpy ndarray
        Array with the best solutions. This array includes z value.


    '''
    num_rows, num_cols = matrix.shape
    lst_feasible = []    # list of feasible solutions
    lst_infeasible = []
    for variables in combinations(range(num_cols), num_rows):
        try:
            vector = np.zeros(num_cols)   # zero vector  [0, 0, 0, ... , 0]
            basic = np.linalg.solve(matrix[:, variables], rhs)
            vector[list(variables)] = basic
            z = objcoef.dot(vector) + constant
            solution = np.concatenate([vector, [z]])   # [x1, x2, x,3] + [zvalue] = [x1, x2, x3, zvalue]
            if np.any(basic < 0):   # infeasible
                lst_infeasible.append(solution)
            else:
                lst_feasible.append(solution)  # feasible solutions
        except np.linalg.LinAlgError:
            print(f"Singular Matrix with variables {variables}")
    feasible_solutions = np.array(lst_feasible)
    infeasible_solutions = np.array(lst_infeasible)  # array of infeasble solutions
    if direction == "max":
        best_index = np.argmax(feasible_solutions[:, -1])  # last column with z value
    else:
        best_index = np.argmin(feasible_solutions[:, -1])
    best_vector = feasible_solutions[best_index]
    return feasible_solutions, infeasible_solutions, best_vector


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


