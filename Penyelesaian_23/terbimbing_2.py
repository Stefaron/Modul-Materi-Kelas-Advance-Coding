produk_toko = {
    "Laptop": {"harga": 15000000, "stok": 10},
    "Smartphone": {"harga": 5000000, "stok": 20},
    "Headset": {"harga": 150000, "stok": 50}
}

# Akses harga dan stok secara langsung
for nama, detail in produk_toko.items():
    harga, stok = detail["harga"], detail["stok"]
    print(f"Produk: {nama}, Harga: {harga}, Stok: {stok}")

