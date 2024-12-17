# Fungsi untuk memeriksa apakah bilangan prima
def cek_prima(bilangan):
    if bilangan < 2:
        return False
    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False
    return True

#Program utama
bilangan = int(input("Masukkan bilangan: "))

if cek_prima(bilangan):
    print(f"{bilangan} adalah bilangan prima.")
else:
    print(f"{bilangan} bukan bilangan prima.")
