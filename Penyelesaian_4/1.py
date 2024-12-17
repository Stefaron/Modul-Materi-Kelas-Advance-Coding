# Fungsi untuk menghitung luas persegi
def hitung_luas(sisi):
    return sisi * sisi

# Fungsi untuk menghitung keliling persegi
def hitung_keliling(sisi):
    return 4 * sisi


# Meminta input dari pengguna
sisi = int(input("Masukkan panjang sisi persegi: "))

# Menghitung luas dan keliling
luas = hitung_luas(sisi)
keliling = hitung_keliling(sisi)

# Menampilkan hasil
print(f"Luas persegi: {luas}")
print(f"Keliling persegi: {keliling}")