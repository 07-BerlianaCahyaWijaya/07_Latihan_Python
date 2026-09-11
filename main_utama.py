import os
import sys

# Jalur aman penemu folder modul
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    BASE_DIR = os.getcwd()

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Import DB Helper
from db_helper import daftar_user, login_user, simpan_riwayat, lihat_riwayat

# Import dari modul-modul temenmu
from rumus_bangun import *
from logika_angka import *

user_aktif = None

def portal_akses():
    global user_aktif
    while True:
        print("\n==========================================")
        print("    SYSTEM PORTAL (LOGIN / REGISTER)    ")
        print("==========================================")
        print("1. Login Akun")
        print("2. Registrasi Akun Baru")
        print("3. Keluar")
        
        opsi = input("Pilih menu (1-3): ")
        
        if opsi == "1":
            print("\n--- LOGIN AKUN ---")
            identifier = input("Email / Username : ")
            pwd = input("Password         : ")
            status, username_res, pesan = login_user(identifier, pwd)
            print(f"-> {pesan}")
            if status:
                user_aktif = username_res
                break
                
        elif opsi == "2":
            print("\n--- REGISTRASI AKUN BARU ---")
            email = input("Email Baru    : ")
            uname = input("Username Baru : ")
            pwd = input("Password Baru : ")
            status, pesan = daftar_user(email, uname, pwd)
            print(f"-> {pesan}")
            
        elif opsi == "3":
            print("\nProgram dihentikan.")
            sys.exit()
        else:
            print("\nPilihan tidak valid.")

def main():
    portal_akses()
    
    while True:
        print("\n==========================================")
        print(f" APLIKASI PERHITUNGAN | Akun: {user_aktif.upper()}")
        print("==========================================")
        print("1. Hitung Luas Persegi")
        print("2. Hitung Keliling Persegi")
        print("3. Cek Bilangan Prima")
        print("4. Cek Bilangan Genap / Ganjil")
        print("5. Hitung Luas Lingkaran")
        print("6. Hitung Luas Segitiga")
        print("7. Lihat Riwayat Tersimpan")
        print("8. Logout & Keluar")
        print("==========================================")
        
        opsi = input("Pilih menu (1-8): ")
        
        if opsi == "1":
            sb = float(input("Masukkan panjang sisi: "))
            hasil = hitung_persegi_luas(sb)
            print(f"Hasil Luas Persegi = {hasil}")
            simpan_riwayat(user_aktif, "Luas Persegi", hasil)
            
        elif opsi == "2":
            sb = float(input("Masukkan panjang sisi: "))
            hasil = hitung_persegi_keliling(sb)
            print(f"Hasil Keliling Persegi = {hasil}")
            simpan_riwayat(user_aktif, "Keliling Persegi", hasil)
            
        elif opsi == "3":
            bil = int(input("Masukkan angka: "))
            if cek_angka_prima(bil):
                print(f"Angka {bil} adalah Bilangan Prima.")
                simpan_riwayat(user_aktif, "Cek Prima", f"{bil} (Bilangan Prima)")
            else:
                print(f"Angka {bil} bukan Bilangan Prima.")
                simpan_riwayat(user_aktif, "Cek Prima", f"{bil} (Bukan Prima)")
                
        elif opsi == "4":
            bil = int(input("Masukkan angka: "))
            res = deteksi_genap_ganjil(bil)
            print(f"Angka {bil} merupakan Bilangan {res}.")
            simpan_riwayat(user_aktif, "Ganjil Genap", f"{bil} ({res})")
                
        elif opsi == "5":
            r = float(input("Masukkan jari-jari: "))
            hasil = hitung_lingkaran_luas(r)
            print(f"Hasil Luas Lingkaran = {hasil}")
            simpan_riwayat(user_aktif, "Luas Lingkaran", hasil)

        elif opsi == "6":
            a = float(input("Masukkan alas: "))
            t = float(input("Masukkan tinggi: "))
            hasil = hitung_segitiga_luas(a, t)
            print(f"Hasil Luas Segitiga = {hasil}")
            simpan_riwayat(user_aktif, "Luas Segitiga", hasil)
            
        elif opsi == "7":
            print(f"\n--- RIWAYAT TERSIMPAN [{user_aktif}] ---")
            print(lihat_riwayat(user_aktif))

        elif opsi == "8":
            print(f"\nLogout dari akun {user_aktif}. Terima kasih!")
            break
        else:
            print("Pilihan tidak tersedia, masukkan angka 1-8!")

if __name__ == "__main__":
    main()
