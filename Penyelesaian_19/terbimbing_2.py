belanja = {}
while True:
    item = input("Nama barang (atau ketik 'stop' buat selesai): ")
    if item == 'stop':
        break
    harga = int(input("Masukin harga barang: "))
    belanja[item] = harga

total = sum(belanja.values())
print("Total harga belanja:", total)

