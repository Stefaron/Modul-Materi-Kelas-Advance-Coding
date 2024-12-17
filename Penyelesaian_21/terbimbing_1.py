stok_gudang = {
    "TV": 4,
    "Kulkas": 7,
    "AC": 2
}

for barang, stok in stok_gudang.items():
    if stok < 5:
        print(f"{barang} stoknya kurang dari 5")

