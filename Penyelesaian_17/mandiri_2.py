def cari_terbesar(angka_list):
    terbesar = angka_list[0]
    for num in angka_list:
        if num > terbesar:
            terbesar = num
    return terbesar


angka_list = input("Masukkan deretan angka, pisahkan dengan spasi: ").split(" ") # Input: 1 3 4

print("Angka terbesar:", cari_terbesar(angka_list)) # Output: 4

