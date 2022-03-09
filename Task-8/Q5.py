import numpy as np

# Q5 (ii)

# Multiplying a matrix

A = np.random.randint(0,3,(3,3))
B = np.random.randint(0,3,(3,4)) 
print('A =\n',A)
print('B =\n',B)
M = np.dot(A,B)
print("")
print('Matrix Multiplication =')

print("")
print(M)
print("")

# Q5 (iii) 

# Identity matrix

I = np.eye(5)
print("Identity Matrix :")
print("")
print(I)
