pendapatan_produk = {
    "Produk X": 500000,
    "Produk Y": 700000,
    "Produk Z": 300000
}

produk_tertinggi = max(pendapatan_produk, key=pendapatan_produk.get)
print(f"Produk dengan pendapatan tertinggi: {produk_tertinggi}")

