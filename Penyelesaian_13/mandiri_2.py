positif = 0
negatif = 0
nol = 0

for i in range(5):
    angka = int(input("Masukkan angka: "))
    if angka > 0:
        positif += 1
    elif angka < 0:
        negatif += 1
    else:
        nol += 1

print("Jumlah angka positif:", positif)
print("Jumlah angka negatif:", negatif)
print("Jumlah angka nol:", nol)
