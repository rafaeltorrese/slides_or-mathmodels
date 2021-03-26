import numpy as np



def create_fullmatrix(body, inequalities, c, direction=1, M=1000):
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
    full_labels = [f"x{i + 1}" for i in range(cols)] + labels
    full_matrix = np.hstack((body, samatrix))

    z = np.concatenate((c, direction * -np.array(zaux)))
    return full_matrix, full_labels, z


if __name__ == "__main__":
    body = np.array([
        [2, 1],
        [1, 3],
        [0, 1],
        ], dtype=float)
    ineqstrings = ["<=", ">=", "<="]
    direction = 1

    c = np.array([3, -1])



    A, labels, cj = create_fullmatrix(body, ineqstrings, c=c, direction=1)

    print(cj)

    print(A)
    print(labels)

    print(cj)
    print(c)