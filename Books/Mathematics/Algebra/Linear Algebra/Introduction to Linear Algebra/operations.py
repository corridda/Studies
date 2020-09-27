import numpy as np

M = np.array([[4, 1, 1, 2, 1],
              [1, 2, -1, 1, 1],
              [3, 1, 1, 1, 1],
              [2, 1, 1, 4, 1],
              [2, -1, 1, 1, 5]])
# det = 64
det = np.linalg.det(M)
print(f"M:\n{M}")
print(f"det M= {round(det)}\n")

print(f"M.T:\n{M.T}")
print(f"det M.T= {round(np.linalg.det(M.T))}\n")

# Compute the determinant of an array.
matr = [[3, -3, 1], [-3, 5, -2], [1, -2, 1]]
print(f"matr: {matr}")
print(f"round(np.linalg.det(matr)): {round(np.linalg.det(matr))}")

# Compute the (multiplicative) inverse of a matrix.
print(f"np.linalg.inv(matr):\n{np.linalg.inv(matr)}\n")

# Matrix product of two arrays
m = np.array([[2, 5, 7], [6, 3, 4], [5, -2, -3]])
m_inv = np.linalg.inv(m)
print(f"np.linalg.matmul(m, m_inv):\n{np.matmul(m, m_inv)}\n")
print(f"np.linalg.matmul(m_inv, m):\n{np.matmul(m_inv, m)}\n")

# Raise a square matrix to the (integer) power n
m = np.array([[0, -1], [3, 2]])
print(f"np.linalg.matrix_power(m, 3):\n{np.linalg.matrix_power(m, 3)}\n")

# Return matrix rank of array using SVD method
m = np.array([[4, -3, 2, -1], [3, -2, 1, -3], [5, -3, 1, -8]])
print(f"np.linalg.matrix_rank(m): {np.linalg.matrix_rank(m)}")
m_ext = np.array([[4, -3, 2, -1, 8], [3, -2, 1, -3, 7], [5, -3, 1, -8, 1]])
print(f"np.linalg.matrix_rank(m): {np.linalg.matrix_rank(m_ext)}\n")

A = np.array([[3, 1, 2], [4, 8, 5], [3, 1, 2]], dtype='int16')
B = np.array([[2, 1, 4], [3, 2, 1], [6, 2, 3]], dtype='int16')
C = np.array([[1, 0, 2], [3, 2, 0], [4, 6, 4]], dtype='int16')
AB = np.dot(A, B)
ABC = np.dot(AB, C)
print(f"AB:\n{AB}\n")
print(f"ABC:\n{ABC}\n")
