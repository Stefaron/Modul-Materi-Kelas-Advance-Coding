serangan = int(input("Masukkan nilai serangan: "))
pertahanan = int(input("Masukkan nilai pertahanan: "))

if serangan > 80:
    if pertahanan > 70:
        print("Pemain menang!")
    else:
        print("Pemain kalah, tetapi bisa melarikan diri")
else:
    print("Pemain langsung kalah")
