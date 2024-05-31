import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Data yang diberikan
x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk interpolasi Lagrange
def lagrange_interpolation(x, y, xi):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (xi - x[j]) / (x[i] - x[j])
        result += term
    return result

# Fungsi untuk interpolasi Newton
def newton_interpolation(x, y):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x[i + j] - x[i])
    
    # Evaluasi polinom Newton
    x_sym = sp.Symbol('x')
    polynomial = coef[0, 0]
    for i in range(1, n):
        term = coef[0, i]
        for j in range(i):
            term *= (x_sym - x[j])
        polynomial += term
    return sp.expand(polynomial)

# Contoh penggunaan
xi = np.linspace(5, 40, 100)  # Nilai yang ingin diinterpolasi (rentang untuk grafik)

# Interpolasi Lagrange
lagrange_result = np.array([lagrange_interpolation(x_data, y_data, x) for x in xi])

# Interpolasi Newton
newton_polynomial = newton_interpolation(x_data, y_data)
newton_result = np.array([newton_polynomial.subs(sp.Symbol('x'), x) for x in xi], dtype=float)

# Plotting hasil interpolasi
plt.figure(figsize=(10, 6))
plt.plot(xi, lagrange_result, label='Lagrange Interpolation', color='blue', linestyle='--')
plt.plot(xi, newton_result, label='Newton Interpolation', color='red', linestyle='-.')
plt.scatter(x_data, y_data, color='black', zorder=5)
plt.title('Interpolasi Lagrange dan Newton')
plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu Patah (jam)')
plt.legend()
plt.grid(True)
plt.show()
