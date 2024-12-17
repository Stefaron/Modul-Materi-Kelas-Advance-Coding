def hitung_total_harga(harga_list):
    return sum(harga_list)

harga_list = []
while True:
    harga = int(input("Masukkan harga barang (0 untuk selesai): ")) # Input: 1000, 500, 2500, 0
    if harga == 0:
        break
    harga_list.append(harga)

print("Total harga:", hitung_total_harga(harga_list)) # Output: 4000

