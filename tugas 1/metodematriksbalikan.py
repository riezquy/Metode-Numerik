import numpy as np

# Metode matriks balikan
def matriks_balikan(A, B):
    # Menghitung matriks balikan dari A
    A_inv = np.linalg.inv(A)
    # Menghitung solusi dengan perkalian matriks balikan dengan B
    X = np.dot(A_inv, B)
    return X

# Kode testing
A = np.array([[2, 3, 4], [1, -1, 2], [3, 4, 5]])
B = np.array([1, 2, 3])

# Metode matriks balikan
X_inv = matriks_balikan(A, B)
print("Solusi dengan metode matriks balikan:", X_inv)
