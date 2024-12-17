with open("contoh.txt", "r") as file:
    baris_baru = [baris.replace("Flask", "Django") for baris in file]

with open("contoh.txt", "w") as file:
    file.writelines(baris_baru)
