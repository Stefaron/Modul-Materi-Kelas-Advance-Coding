barang_toko = {
    ("Elektronik", "TV"): 3000000,
    ("Elektronik", "Laptop"): 10000000,
    ("Pakaian", "Kaos"): 50000,
    ("Pakaian", "Jaket"): 200000
}

cari_kategori = input("Jenis barang apa yang anda cari: ").capitalize()

barang_elektronik = {}
for key, value in barang_toko.items():
    if key[0] == cari_kategori:
        barang_elektronik[key] = value

print("Barang dalam kategori Elektronik:", barang_elektronik)

