import numpy as np

ITERATION_LIMIT = 1000

#initialize the matrix
A = np.array([[10., -1., 2., 0.,],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])
#initialize the RHS vector
b = np.array([6., 25., -1.,15.])

#print persamaan
print("Persamaan : ")
for i in range(A.shape[0]):
    row = ["{}*x{}".format(A[i, j], j +1)
           for j in range(A.shape[1])]
    print(" + ".join(row), "=", b[i])
print()