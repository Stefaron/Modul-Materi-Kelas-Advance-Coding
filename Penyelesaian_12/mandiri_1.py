harga_diskon = lambda harga_awal, diskon: harga_awal - (harga_awal * diskon / 100)

# Contoh penggunaan
print("\nHarga akhir setelah menerima diskon adalah", harga_diskon(1000, 20), "\n")  # Output: 800

