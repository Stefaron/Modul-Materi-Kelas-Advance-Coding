kalimat = "python adalah bahasa pemrograman yang keren, python juga berguna untuk belajar pemrograman"
kata_list = kalimat.split()

# Menghitung frekuensi kemunculan tiap kata
frekuensi_kata = {}
for kata in kata_list:
    if kata in frekuensi_kata:
        frekuensi_kata[kata] += 1
    else:
        frekuensi_kata[kata] = 1

# Tampilkan kata yang muncul lebih dari satu kali
kata_terbanyak = {}
for k, v in frekuensi_kata.items():
    if v > 1:
        kata_terbanyak[k] = v

print("Kata yang muncul lebih dari satu kali:", kata_terbanyak)


