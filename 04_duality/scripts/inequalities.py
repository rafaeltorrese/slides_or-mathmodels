import numpy as np

from algorithms import simplex

def create_fullmatrix(body, inequalities, c, varlabel="x", direction=1, M=1000):
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

    if not isinstance(body,  np.ndarray, ):
        body = np.array(body, dtype=float)

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

    samatrix = np.zeros((rows, len(labels)))
    samatrix[row_positions, range(len(labels))] = signs
    full_labels = [f"{varlabel }{i + 1}" for i in range(cols)] + labels
    full_matrix = np.hstack((body, samatrix))

    z = np.concatenate((c, direction * -np.array(zaux)))
    return full_matrix, full_labels, z


if __name__ == "__main__":
    body_primal = [
        [0.1, 0.0],
        [0.0, 0.1],
        [0.1, 0.2],
        [0.2, 0.1]
        ]

    ineqstrings_primal = [">=", ">=", ">=", ">="]
    sense_primal = -1
    c_primal = [0.07, 0.05]
    b_primal = [0.40, 0.60, 2.00, 1.80]


    A, labels, cj = create_fullmatrix(body_primal, ineqstrings_primal, c=c_primal, direction=sense_primal)

    solprimal, zvalues, lastrows_primal = simplex(matrix=body_primal,
                                                  rhs=b_primal,
                                                  z=c_primal,
                                                  inequalities=ineqstrings_primal,
                                                  direction=sense_primal,
                                                  M=1000,
                                                  vlabel="x")


    body_dual = np.array(body_primal).T
    ineqstrings_dual = ["<=", "<="]
    sense_dual = 1
    c_dual = b_primal[:]
    b_dual = c_primal[:]

    soldual, wvalues, lastrows_dual= simplex(matrix=body_dual,
                                                  rhs=b_dual,
                                                  z=c_dual,
                                                  inequalities=ineqstrings_dual,
                                                  direction=sense_dual,
                                                  M=1000,
                                                  vlabel="y")


