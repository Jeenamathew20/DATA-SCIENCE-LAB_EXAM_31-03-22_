import numpy as np
from numpy.linalg import svd

A =np.array([[2,3,4,5], [2,2,2,2], [1,2,1,2], [3,2,1,3]])
print("matrix:")
print(A)
X,B,T = svd(A)
print("decomposition of matrix:", X)
print("inverse of matrix:", B)
print("transporse of a matrix:", T)

print("perform matrix operations:")

print(np.array(A))
print("addition of two matrix - X+T")
print(np.add(X,T))
print("substraction of two matrix - X-T" )
print(np.subtract(X,T))
print("multiplication of matrix")
print(np.multiply(X,X,X))
D = np.array(X)
print("D:",D)
print("2*X^3")
print(np.multiply(2,D))

