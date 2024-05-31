import numpy as np
import time

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Implementasi Aturan Simpson 1/3
def aturan_simpson(f, a, b, N):
    if N % 2 == 1:
        N += 1  # N harus genap
    h = (b - a) / N
    x = np.linspace(a, b, N+1)
    y = f(x)
    S = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2])
    return (h / 3) * S

# Nilai referensi pi
pi_ref = 3.14159265358979323846

# Fungsi untuk menghitung galat RMS
def galat_rms(aproksimasi, referensi):
    return np.sqrt((aproksimasi - referensi)**2)

# Fungsi pengujian
def uji_aturan_simpson():
    hasil = []
    nilai_N = [10, 100, 1000, 10000]
    
    for N in nilai_N:
        waktu_mulai = time.time()
        pi_approx = aturan_simpson(f, 0, 1, N)
        waktu_selesai = time.time()
        
        galat = galat_rms(pi_approx, pi_ref)
        waktu_eksekusi = waktu_selesai - waktu_mulai
        
        hasil.append({
            'N': N,
            'Aproksimasi Pi': pi_approx,
            'Galat RMS': galat,
            'Waktu Eksekusi': waktu_eksekusi
        })
    
    return hasil

# Menjalankan pengujian
hasil_uji = uji_aturan_simpson()

# Mencetak hasil
for hasil in hasil_uji:
    print(f"N = {hasil['N']}, Aproksimasi Pi = {hasil['Aproksimasi Pi']}, "
          f"Galat RMS = {hasil['Galat RMS']}, Waktu Eksekusi = {hasil['Waktu Eksekusi']} detik")
