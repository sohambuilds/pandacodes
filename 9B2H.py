import numpy as np
a = np.array([[1,2,3],[2,3,4]])
b = np.array([[4,4,5],[2,2,3]])
print(a+b)

ta = np.transpose(a+b)
print(ta)

ra = np.reshape(ta, (6,1))
print(ra)

b = np.reshape(b, (3,2))
dot = np.dot(a,b)
print(dot)

ib = np.linalg.inv(dot)
print(ib)

eigenvalue , eigenvector = np.linalg.eig(ib)

print(eigenvalue,eigenvector)

det = np.linalg.det(ib)
print(det)


