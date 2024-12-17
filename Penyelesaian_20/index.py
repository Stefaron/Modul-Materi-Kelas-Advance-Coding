produk = {"apel": 10, "jeruk": 15, "mangga": 7}
for key in produk:
    print(key)

''' Output:
apel
jeruk
mangga
'''

produk = {"apel": 10, "jeruk": 15, "mangga": 7}
for value in produk.values():
    print(value)

''' Output:
10
15
7
'''

produk = {"apel": 10, "jeruk": 15, "mangga": 7}
for key, value in produk.items():
    print(f"{key} ada sebanyak {value} buah")

''' Output:
apel ada sebanyak 10 buah
jeruk ada sebanyak 15 buah
mangga ada sebanyak 7 buah
'''

produk_detail = {
    "apel": {"harga": 5000, "stok": 10},
    "jeruk": {"harga": 7000, "stok": 15},
    "mangga": {"harga": 8000, "stok": 7}
}

for produk, detail in produk_detail.items():
    print(f"{produk} ->")
    for k, v in detail.items():
        print(f"  {k}: {v}")

produk = {"apel": 10, "jeruk": 15, "mangga": 7}
total_stok = 0

for value in produk.values():
    total_stok += value

print(f"Total stok semua produk: {total_stok}")
# Output: Total stok semua produk: 32

produk = {"apel": 10, "jeruk": 15, "mangga": 7}

stok_terendah = min(produk, key=produk.get)

print(f"Produk dengan stok terendah: {stok_terendah}")
# Output: Produk dengan stok terendah: mangga

