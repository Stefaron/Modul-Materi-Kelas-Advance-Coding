def daftar_terurut():
    barang_list = []
    while True:
        barang = input("Masukkan nama barang (ketik 'selesai' untuk berhenti): ")
        if barang.lower() == "selesai":
            break
        barang_list.append(barang)
        barang_list.sort()
    return barang_list

print("Daftar barang terurut:", daftar_terurut()) # Input: durian, nanas, apel
# Output: Daftar barang terurut: ['apel', 'durian', 'nanas']



