def hitung_jumlah(belanja):
    return len(belanja)

daftar_belanja = []
while True:
    belanjaan = input("Masukan belanja anda, jika sudah ketik '0': ")
    if belanjaan == '0':
        break
    daftar_belanja.append(belanjaan)
    
jumlah = hitung_jumlah(daftar_belanja)
print("Jumlah barang di daftar belanja:", jumlah)

