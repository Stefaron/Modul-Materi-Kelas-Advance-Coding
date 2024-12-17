daftar_tonton = {"Venom", "Avenger", "Superman"}

cek_film = input("Film apa yang anda cari: ").capitalize()

# Cek keberadaan "Film D"
if cek_film not in daftar_tonton:
    print("Film tidak tersedia")
    tanya_tambah = input("Apakah anda ingin menambahkan film tersebut ke daftar? Y/N ").upper()
    if tanya_tambah == "Y":
        daftar_tonton.add(cek_film)

# Hitung jumlah film
jumlah_film = len(daftar_tonton)
print("Daftar tonton:", daftar_tonton)
print("Jumlah film:", jumlah_film)  # Output: 4
