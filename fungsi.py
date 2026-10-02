import math

# === DOKUMEN FUNGSI HITUNG & LOGIKA ===
def hitung_luas_persegi_datar(sisi):
    return sisi * sisi

def hitung_keliling_persegi_datar(sisi):
    return 4 * sisi

def cek_bilangan_prima_logika(n):
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def penentu_genap_ganjil(n):
    if n % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

def hitung_luas_lingkaran_datar(r):
    return 3.14 * r * r

def hitung_luas_segitiga_datar(a, t):
    return 0.5 * a * t


# === SISTEM UTAMA ===
while True:
    print("\n==========================================")
    print("     MODUL PERHITUNGAN & CEK NUMERIK      ")
    print("==========================================")
    print("1. Hitung Luas Persegi")
    print("2. Hitung Keliling Persegi")
    print("3. Cek Bilangan Prima")
    print("4. Cek Bilangan Genap / Ganjil")
    print("5. Hitung Luas Lingkaran")
    print("6. Hitung Luas Segitiga")
    print("7. Keluar")
    print("==========================================")
    
    pilih = input("Pilih menu (1-7): ")
    
    if pilih == "1":
        s = float(input("Masukkan panjang sisi: "))
        print(f"Hasil Luas Persegi -> {hitung_luas_persegi_datar(s)}")
        
    elif pilih == "2":
        s = float(input("Masukkan panjang sisi: "))
        print(f"Hasil Keliling Persegi -> {hitung_keliling_persegi_datar(s)}")
        
    elif pilih == "3":
        ang = int(input("Masukkan nilai angka: "))
        if cek_bilangan_prima_logika(ang):
            print(f"Angka {ang} adalah Bilangan Prima.")
        else:
            print(f"Angka {ang} bukan Bilangan Prima.")
            
    elif pilih == "4":
        ang = int(input("Masukkan nilai angka: "))
        print(f"Angka {ang} adalah Bilangan {penentu_genap_ganjil(ang)}.")
            
    elif pilih == "5":
        r = float(input("Masukkan jari-jari: "))
        print(f"Hasil Luas Lingkaran -> {hitung_luas_lingkaran_datar(r)}")

    elif pilih == "6":
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        print(f"Hasil Luas Segitiga -> {hitung_luas_segitiga_datar(a, t)}")
        
    elif pilih == "7":
        print("Terima kasih, program dihentikan.")
        break
    else:
        print("Pilihan tidak valid, pilih angka 1-7!")