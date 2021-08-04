import numpy as np
import pandas as pd
from auxfunc.algorithms import create_fullmatrix

def dual_simplex(matrix, inequalities, rhs, z):
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
    print("=" * 20, "Dual Simplex Method", "=" * 20)
    matrix = np.array(matrix, dtype=float)
    # if not isinstance(matrix, np.ndarray):
    #     matrix = np.array(matrix, dtype=float)

    num_constraints, numxvars = matrix.shape
    rhs = np.array(rhs)
    z = np.array(z)
    
    matrix, labels, z = create_fullmatrix(matrix, 
                                          inequalities, 
                                          z, 
                                          varlabel="x", 
                                          M=-1000,
                                          direction=1)
    
    cb_index = np.where((matrix == 1) & (np.abs(matrix).sum(axis=0) == 1))[1]
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
        leaving_label = labels[cb_index[leaving]]
        key_row = matrix[leaving]

        if np.all(key_row>=0):
            print("Infeasible Solution")
            break

        ratios = np.divide(net_evaluation, key_row, out=np.full_like(z, np.inf), where=key_row<0)

        entering = ratios.argmin()
        entering_label = labels[entering]

        pivot = matrix[leaving, entering]

        if pivot != 1:
            matrix[leaving] = matrix[leaving] / pivot
            rhs[leaving] = rhs[leaving] / pivot

        for i in range(num_constraints):
            if i == leaving:
                continue
            factor = matrix[i, entering]
            matrix[i] = -factor * matrix[leaving] + matrix[i]
            rhs[i] = -factor * rhs[leaving] + rhs[i]

        cb_index[leaving] = entering

        cb = z[cb_index]
        zj = cb.dot(matrix)
        net_evaluation = z - zj
        
        basic_labels = labels[cb_index]
        
        solution[cb_index] = rhs  # basics

        iteration += 1

        print(f"Iteration {iteration}. {leaving_label} --> {entering_label}")
        print(matrix,  "\n")
        print("Solution", solution, f"\tZ: {cb.dot(rhs):0.2f}", "\n")

        solutions.append(solution)
        fvalues.append(cb.dot(rhs))
        if np.any(net_evaluation > 0):
            print("Method Fails")
            break

        if np.all(net_evaluation <= 0) and np.all(rhs >= 0):            
            print("#" * 20)
            print(f"Optimal solution found in {iteration} iterations")
            print((*zip(labels, np.round(solution, 3))))
            print("\nBasis:")
            print(np.hstack((cb[:,np.newaxis], basic_labels[:,np.newaxis], np.round(rhs[:,np.newaxis], 3))))
            print("\nOptimal Table:")
            print(
                pd.DataFrame(matrix, columns=labels, index=basic_labels)
                )
            print("\nRow Base:")
            print(
                pd.DataFrame(np.vstack((zj, net_evaluation)), 
                             columns=labels,
                             index=["zj", "cj-zj"])
                )
            
                                    
    return np.array(solutions), fvalues, np.vstack((zj, net_evaluation))

if __name__ == '__main__':
    pass