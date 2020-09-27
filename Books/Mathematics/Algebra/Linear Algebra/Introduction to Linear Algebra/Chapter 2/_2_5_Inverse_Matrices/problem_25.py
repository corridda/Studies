import numpy as np

if __name__ == '__main__':
    a = np.array([[2,1,1],
                  [1,2,1],
                  [1,1,2]])
    print(f"np.linalg.inv(a):\n{np.linalg.inv(a)}\n")