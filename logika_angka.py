import math

def cek_angka_prima(n_input):
    if n_input <= 1:
        return False
    for i in range(2, int(math.isqrt(n_input)) + 1):
        if n_input % i == 0:
            return False
    return True

def deteksi_genap_ganjil(n_input):
    if n_input % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"s
