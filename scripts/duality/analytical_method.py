from itertools import combinations
import numpy as np


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