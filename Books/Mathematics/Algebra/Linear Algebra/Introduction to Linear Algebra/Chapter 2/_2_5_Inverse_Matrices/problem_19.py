import numpy as np

if __name__ == '__main__':
    a = np.array([[4, -1, -1, -1],
                  [-1, 4, -1, -1],
                  [-1, -1, 4, -1],
                  [-1, -1, -1, 4]])
    print(f"a:\n{a}\n")
    print(f"np.linalg.inv(a):\n{np.linalg.inv(a)}\n")

    b = np.array([[5, -1, -1, -1, -1],
                  [-1, 5, -1, -1, -1],
                  [-1, -1, 5, -1, -1],
                  [-1, -1, -1, 5, -1],
                  [-1, -1, -1, -1, 5]])
    print(f"b:\n{b}\n")
    print(f"np.linalg.inv(b):\n{np.linalg.inv(b)}")