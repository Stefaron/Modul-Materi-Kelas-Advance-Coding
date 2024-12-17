def hitung_barang(barang_list, barang_dihitung):
    return barang_list.count(barang_dihitung)


barang_list = input("Masukkan daftar barang, pisahkan dengan koma: ").split(", ") # Input: topi, dompet, topi
barang_dihitung = input("Masukkan nama barang yang ingin dihitung: ") # Input: topi

print("Jumlah barang dicari:", hitung_barang(barang_list, barang_dihitung)) # Output: Jumlah barang tersebut: 2

