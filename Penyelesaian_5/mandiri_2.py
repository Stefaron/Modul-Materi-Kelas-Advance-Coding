angka_tebakan = int(input("Tebak angka antara 1 hingga 10: "))

angka_benar = 7

if angka_tebakan < 1 or angka_tebakan > 10:
    print("Tebakan tidak valid")
elif angka_tebakan == angka_benar:
    print("Tebakan benar!")
else:
    print("Tebakan salah!")
