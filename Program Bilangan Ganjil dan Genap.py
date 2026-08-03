# Meminta input angka dari pengguna
angka = int(input("Masukkan sebuah bilangan: "))

# Memeriksa apakah sisa bagi angka dengan 2 adalah 0
if angka % 2 == 0:
    print(f"Bilangan {angka} adalah GENAP.")
else:
    print(f"Bilangan {angka} adalah GANJIL.")