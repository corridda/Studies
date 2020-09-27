import numpy as np

if __name__ == '__main__':
    A = np.array([[2,2],[6,4]])
    print(f"A:\n{A}\n")
    for i in range(len(A[1])):
        A[1][i] -= A[0][i]*3
    print(f"A:\n{A}")