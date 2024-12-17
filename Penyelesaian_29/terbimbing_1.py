with open("contoh.txt", "r") as file:
    for baris in file:
        if "Python" in baris:
            print(baris.strip())

