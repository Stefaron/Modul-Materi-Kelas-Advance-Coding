hewan_peliharaan = ("kucing", "anjing", "burung")

print(hewan_peliharaan)
# Output: ('kucing', 'anjing', 'burung')

# hewan_peliharaan[1] = "kelinci"  # Ini bakal error!

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
tuple3 = (1, 2, 3)

print(tuple1 == tuple3)  # Hasilnya True, karena isinya persis sama
print(tuple1 < tuple2)   # Hasilnya True, karena elemen pertama yang beda lebih kecil

koordinat = (10, 20)
x, y = koordinat  # x jadi 10, y jadi 20
print(f"x: {x}, y: {y}")

a = 5
b = 10
a, b = b, a  # a jadi 10, b jadi 5
print(f"a: {a}, b: {b}")

hasil_tes = {
    ("Andi", "Matematika"): 85,
    ("Andi", "Fisika"): 90,
    ("Budi", "Matematika"): 78
}

# Mengakses nilai berdasarkan key tuple
print(hasil_tes[("Andi", "Matematika")])  # Output: 85

lokasi = {
    (10, 20): "Toko A",
    (30, 40): "Toko B"
}
print(lokasi[(10, 20)])  # Outputnya: Toko A

produk = {"nama": "Laptop", "harga": 15000, "stok": 5}

# Unpack dictionary ke variabel terpisah
nama, harga, stok = produk.values()
print(f"Nama: {nama}, Harga: {harga}, Stok: {stok}")


teks = "saya suka python python sangat menyenangkan suka"
kata_list = teks.split()

# Buat dictionary frekuensi
frekuensi = {}
for kata in kata_list:
    if kata in frekuensi:
        frekuensi[kata] += 1
    else:
        frekuensi[kata] = 1

print(frekuensi)

hasil_tes = {
    ("Andi", "Matematika"): 85,
    ("Andi", "Fisika"): 90,
    ("Budi", "Matematika"): 78
}

print(hasil_tes[("Andi", "Matematika")])  # Outputnya: 85
