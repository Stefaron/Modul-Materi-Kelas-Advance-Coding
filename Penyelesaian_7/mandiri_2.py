# Meminta jumlah pertandingan
total_kill = 0

# Perulangan untuk meminta jumlah kill setiap pertandingan
for i in range(1, 6):
    kill = int(input(f"Masukkan jumlah kill pada pertandingan ke-{i}: "))
    total_kill += kill

# Menampilkan total kill yang didapatkan
print(f"Total kill dalam 5 pertandingan: {total_kill}")
