def cek_kesuksesan(waktu, poin):
    if waktu < 10 and poin > 80:
        return "Balapan sukses!"
    else:
        return "Balapan gagal!"

# Contoh penggunaan
waktu = int(input("Berapa kecepatannya: "))
poin = int(input("Berapa poinnya: "))
print(cek_kesuksesan(waktu, poin))  # Output: Balapan sukses!


