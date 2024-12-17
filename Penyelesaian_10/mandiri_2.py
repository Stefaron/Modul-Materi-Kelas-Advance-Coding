baris = 1

while baris <= 5:  # Mulai dari baris 1 sampai 5
    kolom = 1
    while kolom <= baris:  # Cetak bintang sebanyak nilai 'baris'
        print("*", end="")
        kolom += 1
    print("")  # Pindah ke baris baru
    baris += 1  # Naik ke baris berikutnya
