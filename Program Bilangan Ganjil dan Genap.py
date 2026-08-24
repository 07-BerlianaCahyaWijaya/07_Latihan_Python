# Meminta input angka dari pengguna
angka = int(input("Masukkan sebuah bilangan: "))

# Memeriksa apakah sisa bagi angka dengan 2 adalah 0
if angka % 2 == 0:
    print(f"Bilangan {angka} adalah GENAP.")
else:
    print(f"Bilangan {angka} adalah GANJIL.")

 # Perulangan akan terus berjalan selama variabel lanjut bernilai 'y' atau 'Y'
    while lanjut.lower() == "y":
        # 1. Input bilangan dari pengguna
        bilangan = int(input("\nMasukkan sebuah bilangan: "))
    
        # 2. Logika Modulus (sisa pembagian dengan 2)
        if bilangan % 2 == 0:
            print(f"--> {bilangan} adalah bilangan GENAP")
        else:
            print(f"--> {bilangan} adalah bilangan GANJIL")
    
        # 3. Menanyakan apakah pengguna ingin mengulang atau keluar
        lanjut = input(
            "\nApakah ingin mengecek bilangan lain? (y/n untuk keluar): "
        )
    
    print("\nProgram selesai. Terima kasih telah menggunakan program ini!")
