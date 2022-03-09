import numpy as np

A = np.array([10, 11, 12, 13, 14])
print(A)
nz = 5
Z = np.zeros(len(A) + (len(A)-1)*(nz))
Z[::nz+1] = A
print("")
print(Z)
