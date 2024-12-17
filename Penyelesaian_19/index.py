kontak = {
    "Dio": "081234567890",
    "Rara": "081098765432",
    "Udin": "082233445566"
}

# contoh dictionary kosong
data = {}

# atau bisa juga langsung diisi seperti:
peserta_REC = {"nama": "Budi", "umur": 8, "alamat": "Jongke"}

peserta_REC["kelas"] = "Programming"  # menambahkan key baru
peserta_REC["umur"] = 9  # mengubah value dari key "umur"

print(peserta_REC) 
# Output: {'nama': 'Budi', 'umur': 9, 'alamat': 'Jongke', 'kelas': 'Programming'}

print(peserta_REC["nama"])  # Output: "Budi"
print(peserta_REC["alamat"])  # Output: "Jongke"

del peserta_REC["alamat"]
print(peserta_REC) 
# Output: {'nama': 'Budi', 'umur': 9, 'kelas': 'Programming'}

buah = {"apel": 5, "jeruk": 10, "pisang": 7}
print(len(buah))  # Output: 3

barang = {"buku": 10, "pulpen": 5, "pensil": 3}
print("buku" in barang)   # Output: True
print("penghapus" in barang)  # Output: False

skor = {"Dio": 95, "Rara": 88, "Udin": 75}
print(skor.get("Rara"))      # Output: 88
print(skor.get("Lia", 0))  # Output: 0

