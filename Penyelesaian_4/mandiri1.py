# Menerima input berat barang
berat = float(input("Masukkan berat barang (dalam kg): "))

# Tarif dasar dan biaya per kg
tarif_dasar = 10000
biaya_per_kg = 3000

# Menghitung total biaya pengiriman
total_biaya = tarif_dasar + (berat * biaya_per_kg)

# Mencetak total biaya pengiriman
print("Total biaya pengiriman adalah: Rp", total_biaya)
