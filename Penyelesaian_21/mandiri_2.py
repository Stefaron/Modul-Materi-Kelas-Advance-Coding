harga_kategori = {
    "Elektronik": {"TV": 3000000, "AC": 5000000},
    "Perabot": {"Meja": 500000, "Kursi": 200000}
}

for kategori, barang in harga_kategori.items():
    harga_min = min(barang.values())
    print(f"Harga terendah di kategori {kategori}: Rp{harga_min}")

