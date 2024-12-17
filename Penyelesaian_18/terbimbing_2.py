def buat_daftar_belanja():
    belanjaan = []
    while True:
        barang = input("Masukkan nama barang (ketik 'selesai' untuk berhenti): ")
        # Input: topi, celana, tas
        if barang.lower() == "selesai":
            break
        belanjaan.append(barang)
    return belanjaan

print("Daftar belanjaan:", buat_daftar_belanja()) # Output: ['topi', 'buah', 'celana']

