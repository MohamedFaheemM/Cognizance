import numpy as np

X = np.random.randint(0,2,6)
Y = np.random.randint(0,2,6)
print(X)
print(Y)
equal = np.allclose(X,Y)
print(equal)
