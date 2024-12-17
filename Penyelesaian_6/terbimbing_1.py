kecepatan = int(input("Masukkan kecepatan: "))
akurasi = int(input("Masukkan akurasi: "))
if kecepatan > 80:
    if akurasi > 70:
        print("Juara 1")
    else:
        print("Juara 2")
else:
    print("Tidak Juara")


