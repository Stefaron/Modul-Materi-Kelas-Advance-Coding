poin = int(input("Masukkan poin karakter: "))
bonus = input("Apakah Anda mendapat bonus? (ya/tidak): ").lower()

if poin > 1000:
    if bonus == "ya":
        print("Karakter naik 2 level")
    else:
        print("Karakter naik 1 level")
else:
    print("Karakter tetap di level saat ini")
