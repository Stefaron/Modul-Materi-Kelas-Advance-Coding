# Meminta hasil 20 pertandingan
total_kemenangan = 0
total_pertandingan = 5

# Perulangan untuk meminta hasil setiap pertandingan
for i in range(total_pertandingan):
    hasil = input(f"Hasil pertandingan ke-{i+1} (menang/kalah): ").lower()
    
    if hasil == "menang":
        total_kemenangan += 1

# Menghitung persentase kemenangan
persentase_kemenangan = (total_kemenangan / total_pertandingan) * 100

# Menampilkan persentase kemenangan
print(f"Persentase kemenangan kamu: {persentase_kemenangan}%")
