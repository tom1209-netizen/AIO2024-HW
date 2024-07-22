import numpy as np


def compute_eigenvector_eigenvalue(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


matrix = np.array([[1, 2], [3, 4]])
print(compute_eigenvector_eigenvalue(matrix))