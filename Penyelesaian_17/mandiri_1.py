def cari_inisial(barang_list, inisial):
    hasil = []
    for barang in barang_list:
        if barang.startswith(inisial):
            hasil.append(barang)
    return hasil

barang_list = input("Masukkan daftar barang, pisahkan dengan koma: ").split(", ") # Input: tas, topi, koper
inisial = input("Masukkan huruf inisial: ") # Input: t

print("Barang yang diawali inisial tersebut:", cari_inisial(barang_list, inisial)) # Output: ['topi', 'tas']



