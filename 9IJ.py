import numpy as np


a = np.array([[2,23,4],[4,1,23],[23,14,5]])
b = np.array([12,4,2])

sol = np.linalg.solve(a,b)
print(sol)

U,S,V = np.linalg.svd(a)

print(U,S,V)
