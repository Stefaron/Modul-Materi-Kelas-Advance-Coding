# Bikin list kosong
barang = []

# Bikin list berisi buah-buahan
buah = ["apel", "pisang", "ceri"]

# List berisi macam-macam tipe data
campuran = ["apel", 3.14, 7, True]

barang = ["tas", "sepatu", "topi"]
print(barang[0])  # Output: tas

barang = ["tas", "sepatu", "topi"]
barang[1] = "jaket"  # Ganti "sepatu" jadi "jaket"
print(barang)  # Output: ['tas', 'jaket', 'topi']

koleksi = ["jaket", 42, 3.14, False]
print(koleksi[2]) # Output: 3.14

angka = [1, 2, 2, 3, 4, 4]
print(angka)  # Output: [1, 2, 2, 3, 4, 4]

barang = ["tas", "sepatu", "topi"]
print(barang[0])  # Output: tas

barang = ["tas", "sepatu"]
barang.append("topi")  # Tambah "topi" di akhir
print(barang)  # Output: ["tas", "sepatu", "topi"]

barang.insert(1, "jaket")  # Tambah "jaket" di posisi kedua
print(barang)  # Output: ["tas", "jaket", "sepatu", "topi"]

barang = ["tas", "jaket", "sepatu", "topi"]
barang.remove("sepatu")
print(barang)  # Output: ["tas", "jaket", "topi"]

barang.pop(1)
print(barang)  # Output: ["tas", "topi"]

barang.pop()
print(barang) # Output: ["tas"]

barang = ["tas", "sepatu", "topi"]
print(len(barang))  # Output: 3

barang1 = ["tas", "sepatu"]
barang2 = ["topi", "kacamata"]
gabungan = barang1 + barang2 
print(gabungan)  # Output: ["tas", "sepatu", "topi", "kacamata"]

barang1.extend(barang2)
print(barang1)  # Output: ["tas", "sepatu", "topi", "kacamata"]

barang = ["tas", "sepatu", "topi"]
print("sepatu" in barang)  # Output: True

