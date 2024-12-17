def jumlahkan_angka(harga):
    return sum(harga)

daftar_harga = []
while True:
    input_harga = int(input("Masukkan harga setiap barang, jika sudah inputkan 0: "))
    # Input: 1000, 2000, 3000

    if(input_harga) == 0:
        break
    daftar_harga.append(input_harga)

print("Total harga barang:", jumlahkan_angka(daftar_harga)) # Output: 6000


