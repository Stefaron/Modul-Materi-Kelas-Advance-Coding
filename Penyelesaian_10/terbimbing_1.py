baris = 1

while baris <= 4:  # Loop untuk baris
    kolom = 1
    while kolom <= 4:  # Loop untuk kolom
        print("*", end=" ")  # Cetak bintang dengan spasi
        kolom += 1
    print("")  # Pindah ke baris baru setelah selesai satu baris
    baris += 1
