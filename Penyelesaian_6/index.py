# nilai = int(input('Masukkan nilai: '))
# usia = int(input('Masukkan usia: '))

# if nilai >= 75:
#   if (usia < 15):
#     print('Selamat adek, kamu lulus!')
#   else:
#     print('Selamat kakak, kamu lulus!')
# else:
#   if (usia < 15):
#     print('Mohon maaf dek, coba lagi ya!')
#   else:
#     print('Mohon maaf kak, coba lagi ya!')

# # Menerima input skor ujian dari pengguna
# skor = float(input("Masukkan skor ujian (0-100): "))

# # Memeriksa kategori skor menggunakan nested if
# if skor >= 80:
#     # Skor 80 ke atas
#     nilai = "A"
#     if skor >= 90:
#         keterangan = "Lulus dengan pujian"
#     else:
#         keterangan = "Lulus"
# elif skor >= 65:
#     # Skor 65 - 79
#     nilai = "B"
#     if skor >= 75:
#         keterangan = "Lulus"
#     else:
#         keterangan = "Lulus, perlu peningkatan"
# elif skor >= 50:
#     # Skor 50 - 64
#     nilai = "C"
#     keterangan = "Lulus, perlu banyak belajar"
# elif skor >= 35:
#     # Skor 35 - 49
#     nilai = "D"
#     keterangan = "Tidak Lulus, coba lagi"
# else:
#     # Skor di bawah 35
#     nilai = "E"
#     keterangan = "Tidak Lulus, sangat perlu bimbingan"

# # Mencetak hasil
# print("Nilai Anda:", nilai)
# print("Keterangan:", keterangan)

# Meminta input usia dan hari dari pengguna
usia = int(input("Masukkan usia Anda: "))
hari = input("Masukkan hari kunjungan (contoh: Senin): ").lower()

# Nested if untuk menentukan harga tiket berdasarkan usia dan hari
if usia < 12:
    if hari in ["sabtu", "minggu"]:
        harga_tiket = 25000
    else:
        harga_tiket = 20000
elif 12 <= usia <= 60:
    if hari in ["sabtu", "minggu"]:
        harga_tiket = 50000
    else:
        harga_tiket = 40000
else:  # Usia di atas 60
    if hari in ["sabtu", "minggu"]:
        harga_tiket = 35000
    else:
        harga_tiket = 30000

# Menampilkan harga tiket
print(f"Harga tiket Anda adalah: {harga_tiket}")



