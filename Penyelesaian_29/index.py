with open("contoh.txt", "r") as file:
    # Membaca file baris per baris
    for baris in file:
        if "python" in baris:  # Percabangan untuk mencari kata "python"
            print("Ditemukan kata 'python':", baris.strip())

kata_dicari = "python"
jumlah_kata = 0

with open("contoh.txt", "r") as file:
    for baris in file:
        # Menghitung berapa kali kata_dicari muncul di baris tersebut
        jumlah_kata += baris.lower().split().count(kata_dicari)

print(f"Kata '{kata_dicari}' ditemukan sebanyak {jumlah_kata} kali.")


kata_hapus = "bahasa"
with open("contoh.txt", "r") as file:
    baris_baru = []
    for baris in file:
        if kata_hapus not in baris:  # cek apakah kata 'bahasa' ada
            baris_baru.append(baris)

with open("contoh.txt", "w") as file:
    file.writelines(baris_baru)  # Menulis ulang file tanpa 'bahasa'

