with open("contoh.txt", "r+") as file:
    baris_baru = "Belajar Python itu menyenangkan!\n"
    file_content = file.readlines()

    if len(file_content) == 0:
        file.write(baris_baru)
