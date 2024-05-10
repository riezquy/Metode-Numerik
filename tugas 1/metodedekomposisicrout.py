import numpy as np


# Metode dekomposisi Crout
def dekomposisi_Crout(A, B):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            U[i,j] = A[i,j] - np.dot(L[i,:i], U[:i,j])
        for j in range(i, n):
            if i == j:
                L[i,j] = 1
            else:
                L[j,i] = (A[j,i] - np.dot(L[j,:i], U[:i,i])) / U[i,i]
    Y = np.linalg.solve(L, B)
    X = np.linalg.solve(U, Y)
    return X

# Kode testing
A = np.array([[2, 3, 4], [1, -1, 2], [3, 4, 5]])
B = np.array([1, 2, 3])

# Metode dekomposisi Crout
X_crout = dekomposisi_Crout(A, B)
print("Solusi dengan metode dekomposisi Crout:", X_crout)