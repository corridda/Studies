import numpy as np
from matplotlib import pyplot as plt

A = np.array([[2,-1,0,0,0,0,0,0,0],
              [-1,2,-1,0,0,0,0,0,0],
              [0,-1,2,-1,0,0,0,0,0],
              [0,0,-1,2,-1,0,0,0,0],
              [0,0,0,-1,2,-1,0,0,0],
              [0,0,0,0,-1,2,-1,0,0],
              [0,0,0,0,0,-1,2,-1,0],
              [0,0,0,0,0,0,-1,2,-1],
              [0,0,0,0,0,0,0,-1,2]])

b = np.array([10,10,10,10,10,10,10,10,10])

y = np.linalg.solve(A, b)
print(f"np.linalg.solve(A, b): {y}")
x = np.array(list(range(1,10)))
print(x)
plt.plot(x,y)
plt.show()