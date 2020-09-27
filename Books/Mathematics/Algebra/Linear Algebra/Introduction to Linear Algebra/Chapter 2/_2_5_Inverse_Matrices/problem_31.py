import numpy as np

if __name__ == '__main__':
    a = np.array([[1, -1, 1, -1],
                  [0, 1, -1, 1],
                  [0, 0, 1, -1],
                  [0, 0, 0, 1]])
    print(f"a:\n{a}\n")
    print(f"np.linalg.inv(a):\n{np.linalg.inv(a)}\n")
