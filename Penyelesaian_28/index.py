# Membuka file untuk membaca
# with open("contoh.txt", "r") as file:
#     data = file.read()
#     print(data)

with open("contoh.txt", "r") as file:
    print(file.readline())  # Membaca baris pertama
    print(file.readline())  # Membaca baris kedua

with open("contoh.txt", "r") as file:
    lines = file.readlines()
    print(lines)


with open("contoh.txt", "w") as file:
    file.write("Isi baru file ini.")

with open("contoh.txt", "a") as file:
    file.write("\nIni tambahan baris baru.")

