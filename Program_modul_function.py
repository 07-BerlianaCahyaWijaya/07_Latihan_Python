import math

# === DOKUMEN FUNGSI MATEMATIKA & LOGIKA ===
def hitung_persegi_luas(sisi_bangun):
    return sisi_bangun * sisi_bangun

def hitung_persegi_keliling(sisi_bangun):
    return 4 * sisi_bangun

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
        return "Ganjil"

def hitung_lingkaran_luas(r_lingkaran):
    return 3.14 * r_lingkaran * r_lingkaran

def hitung_segitiga_luas(a_segitiga, t_segitiga):
    return 0.5 * a_segitiga * t_segitiga


# === EKSEKUSI MENU UTAMA ===
while True:
    print("\n==========================================")
    print("    APLIKASI PERHITUNGAN & CEK ANGKA     ")
    print("==========================================")
    print("1. Hitung Luas Persegi")
    print("2. Hitung Keliling Persegi")
    print("3. Cek Bilangan Prima")
    print("4. Cek Bilangan Genap / Ganjil")
    print("5. Hitung Luas Lingkaran")
    print("6. Hitung Luas Segitiga")
    print("7. Keluar")
    print("==========================================")
    
    opsi = input("Pilih menu (1-7): ")
    
    if opsi == "1":
        sb = float(input("Masukkan panjang sisi: "))
        print(f"Hasil Luas Persegi = {hitung_persegi_luas(sb)}")
        
    elif opsi == "2":
        sb = float(input("Masukkan panjang sisi: "))
        print(f"Hasil Keliling Persegi = {hitung_persegi_keliling(sb)}")
        
    elif opsi == "3":
        bil = int(input("Masukkan angka: "))
        if cek_angka_prima(bil):
            print(f"Angka {bil} adalah Bilangan Prima.")
        else:
            print(f"Angka {bil} bukan Bilangan Prima.")
            
    elif opsi == "4":
        bil = int(input("Masukkan angka: "))
        print(f"Angka {bil} merupakan Bilangan {deteksi_genap_ganjil(bil)}.")
            
    elif opsi == "5":
        r = float(input("Masukkan jari-jari: "))
        print(f"Hasil Luas Lingkaran = {hitung_lingkaran_luas(r)}")

    elif opsi == "6":
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        print(f"Hasil Luas Segitiga = {hitung_segitiga_luas(a, t)}")
        
    elif opsi == "7":
        print("Program dihentikan, terima kasih!")
        break
    else:
        print("Pilihan tidak tersedia, masukkan angka 1-7!")
