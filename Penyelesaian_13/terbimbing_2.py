kata_rahasia = "PYTHON"
tebakan = ""

while tebakan != kata_rahasia:
    tebakan = input("Tebak kata rahasia: ").upper()
    if tebakan != kata_rahasia:
        print("Salah, coba lagi.")
    else:
        print("Selamat! Tebakanmu benar.")

