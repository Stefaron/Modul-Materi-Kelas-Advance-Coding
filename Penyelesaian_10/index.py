# listKota = [
#   'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
#   'Jogjakarta', 'Semarang', 'Makassar'
# ]

# # skip jika i adalah bilangan genap
# # dan i lebih dari 0
# i = -1
# while i < len(listKota):
#   i += 1
#   if i % 2 == 0 and i > 0:
#     print('skip')
#     continue

#   # tidak dieksekusi ketika continue dipanggil
#   print(listKota[i])


# listKota = [
#   'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
#   'Jogjakarta', 'Semarang', 'Makassar'
# ]

# kotaYangDicari = input('Masukkan nama kota yang dicari: ')

# i = 0
# while i < len(listKota):
#   if listKota[i].lower() == kotaYangDicari.lower():
#     print('Ketemu di index', i)
#     break

#   print('Bukan', listKota[i])
#   i += 1

i = 1  # Mulai dari angka 1 untuk baris

while i <= 5:  # Loop luar, i mewakili baris
    j = 1  # Mulai dari angka 1 untuk kolom
    while j <= 5:  # Loop dalam, j mewakili kolom
        print(f"{i} x {j} = {i * j}", end="\t")  # Cetak hasil perkalian
        j += 1  # Tambah j
    print("")  # Pindah ke baris baru
    i += 1  # Tambah i
