# Membaca file baris per baris
with open("daftar_belanja.txt", "r") as file:
    for line in file:
        print(line.strip())
