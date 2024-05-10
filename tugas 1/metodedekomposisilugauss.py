import numpy as np

# Metode dekomposisi LU Gauss
def dekomposisi_LU_Gauss(A, B):
    n = len(A)
    # Inisialisasi matriks L sebagai matriks identitas
    L = np.eye(n)
    # Salin matriks A ke matriks U dan konversi ke float
    U = np.copy(A).astype(float)
    for k in range(n-1):
        for i in range(k+1, n):
            # Hitung faktor untuk mengurangi baris ke-i
            factor = U[i,k] / U[k,k]
            L[i,k] = factor
            # Kurangi baris ke-i dengan faktor * baris ke-k
            U[i,k:] -= factor * U[k,k:]
    # Selesaikan sistem persamaan linear menggunakan matriks L dan U
    Y = np.linalg.solve(L, B)
    X = np.linalg.solve(U, Y)
    return X


# Metode dekomposisi LU Gauss
X_lu_gauss = dekomposisi_LU_Gauss(A, B)
print("Solusi dengan metode dekomposisi LU Gauss:", X_lu_gauss)