total_genap = 0

for i in range(10):
    angka = int(input("Masukkan angka: "))
    if angka % 2 == 0:
        total_genap += angka

print("Jumlah total angka genap yang dimasukkan:", total_genap)
