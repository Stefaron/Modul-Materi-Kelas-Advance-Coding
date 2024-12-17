kata_dicari = "Python"
jumlah_kata = 0

with open("contoh.txt", "r") as file:
    for baris in file:
        jumlah_kata += baris.lower().split().count(kata_dicari.lower())

print(f"Kata '{kata_dicari}' ditemukan sebanyak {jumlah_kata} kali.")

