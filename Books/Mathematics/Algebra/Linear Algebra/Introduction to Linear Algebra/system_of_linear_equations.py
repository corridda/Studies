"""System of linear equations"""
# https://en.wikipedia.org/wiki/System_of_linear_equations

import numpy as np


def system_is_consistent(A: np.array, b: np.array) -> bool:
    """Explore the system consistency.

    According to the Rouché–Capelli theorem (Kronecker–Capelli theorem),
    any system of equations (overdetermined or otherwise)
    is inconsistent if the rank of the augmented matrix is greater than the rank of the coefficient matrix.
    """
    A_ext = np.hstack([A, b[:, np.newaxis]])
    return np.linalg.matrix_rank(A) == np.linalg.matrix_rank(A_ext)


def matrix_solution(A: np.array, b: np.array) -> np.array:
    """Matrix solution of linear system.

    If the matrix A is square (has m rows and n=m columns) and has full rank (all m rows are independent),
    then the system has a unique solution given by
    x = A**{-1} * b """
    if system_is_consistent(A, b):
        if (A.shape[0] == A.shape[1]) and (np.linalg.det(A) != 0):
            return np.matmul(np.linalg.inv(A), b)
        raise np.linalg.LinAlgError
    else:
        raise np.linalg.LinAlgError("The linear system is inconsistent.")


def rule_of_Cramer(A: np.array, b: np.array) -> np.array:
    """Solution of linear system with Cramer's rule."""
    if system_is_consistent(A, b):
        main_det = np.linalg.det(A)
        if (A.shape[0] == A.shape[1]) and (main_det != 0):
            numerators = np.zeros((A.shape[1]))
            for i in range(A.shape[0]):
                A_copy = np.copy(A)
                for j in range(len(A_copy)):
                    A_copy[j][i] = b[j]
                numerators[i] = np.linalg.det(A_copy)
            return numerators / main_det
        raise np.linalg.LinAlgError
    else:
        raise np.linalg.LinAlgError("The linear system is inconsistent.")


def main():
    # Matrix solution
    A = np.array([[2, -1], [1, 3]])
    b = np.array([0, 7])
    print(f"matrix_solution(A, b): {matrix_solution(A, b)}\n")

    # Cramer's rule
    print(f"rule_of_Cramer(A, b): {rule_of_Cramer(A, b)}\n")
    print(f"rule_of_Cramer(_, _): {rule_of_Cramer(np.array([[2,-3,1],[2,1,-4],[6,-5,2]]), np.array([2,9,17]))}\n")

    # built-in solution
    print(f"np.linalg.solve(A, b): {np.linalg.solve(A, b)}\n")
    print(f"np.linalg.solve(_, _): {np.linalg.solve(np.array([[3,-2,4],[3,4,-2],[2,-1,-1]]), np.array([21,9,10]))}\n")

    #  raise np.linalg.LinAlgError("The linear system is inconsistent.")
    # A = np.array([[4,-3,2,-1],[3,-2,1,-3],[5,-3,1,-8]])
    # b = np.array([8,7,1])
    # print(f"np.linalg.solve(A, b): {np.linalg.solve(A, b)}\n")
    # print(f"matrix_solution(A, b): {matrix_solution(A, b)}\n")
    # print(f"rule_of_Cramer(A, b): {rule_of_Cramer(A, b)}\n")

    #  raise np.linalg.LinAlgError("The linear system is inconsistent.")
    # A = np.array([[7,-2,-1],[6,-4,-5],[1,2,4]])
    # b = np.array([2,3,5])
    # print(f"np.linalg.solve(A, b): {np.linalg.solve(A, b)}\n")
    # print(f"matrix_solution(A, b): {matrix_solution(A, b)}\n")
    # print(f"rule_of_Cramer(A, b): {rule_of_Cramer(A, b)}\n")


    # Return the least-squares solution to a linear matrix equation.
    A = np.array([[2,3,-1,1],[8,12,-9,8],[4,6,3,-2],[2,3,9,-7]])
    b = np.array([1,3,3,3])
    # print(f"np.linalg.solve(A, b): {np.linalg.solve(A, b)}\n")
    try:
        print(f"matrix_solution(A, b): {matrix_solution(A, b)}\n")
    except np.linalg.LinAlgError as e:
        print(repr(e))
    print(f"{np.linalg.lstsq(A, b, rcond=None)}\n")



if __name__ == '__main__':
    main()
