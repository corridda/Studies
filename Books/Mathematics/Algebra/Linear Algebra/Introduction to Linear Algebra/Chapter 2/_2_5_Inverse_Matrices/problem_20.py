import numpy as np

if __name__ == '__main__':
    a = np.array([[3, -1, -1, -1],
                  [-1, 3, -1, -1],
                  [-1, -1, 3, -1],
                  [-1, -1, -1, 3]])
    ones = np.array([[1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 1, 1]])
    print(f"np.dot(a, ones):\n{np.dot(a, ones)}\n")