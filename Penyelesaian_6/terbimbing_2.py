usia = int(input("Masukkan usia: "))
berat = int(input("Masukkan berat badan: "))
if usia < 18:
    if berat < 50:
        print("Kurus")
    else:
        print("Sehat")
else:
    print("Tidak berlaku untuk usia dewasa")


