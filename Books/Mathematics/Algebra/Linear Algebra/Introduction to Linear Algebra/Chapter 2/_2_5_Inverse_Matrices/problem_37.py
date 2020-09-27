import numpy as np

if __name__ == '__main__':
    P = np.array([[1,1,1,1],[1,2,3,4],[1,3,6,10],[1,4,10,20]])
    print(f"P:\n{P}\n")
    print(f"np.linalg.inv(P):\n{np.linalg.inv(P)}\n")

    L = np.array([[1,0,0,0],[1,1,0,0],[1,2,1,0],[1,3,3,1]])
    P = np.matmul(L, L.T)
    print(f"P:\n{P}")
