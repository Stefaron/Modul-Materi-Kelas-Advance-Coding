# Jumlah keranjang
jumlah_keranjang = 5

# Jumlah apel di setiap keranjang
apel_per_keranjang = 3

# Variabel untuk menyimpan total apel
total_apel = 0

# Menggunakan perulangan untuk menghitung total apel
for keranjang in range(jumlah_keranjang):
    total_apel += apel_per_keranjang
    print(f"Keranjang ke-{keranjang + 1}, total apel sekarang: {total_apel}")

# Cetak total apel
print(f"Total apel yang kamu miliki: {total_apel}")


