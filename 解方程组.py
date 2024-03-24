import numpy as np

coefficients = np.array([[3, 0, 0], [2, 1, 0], [0, 1, -2]])
constants = np.array([20040, 19640, -14960])

solutions = np.linalg.solve(coefficients, constants)

pass




