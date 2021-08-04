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
    return full_matrix, np.array(full_labels), cj