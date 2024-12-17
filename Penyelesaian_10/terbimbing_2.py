password_rahasia = "gamer123"
kesempatan = 3

while kesempatan > 0:
    tebakan = input("Masukkan password: ")
    if tebakan == password_rahasia:
        print("Password benar! Kamu berhasil masuk.")
        break  # Keluar dari loop jika password benar
    else:
        kesempatan -= 1  # Kurangi kesempatan
        print(f"Salah! Kesempatan tersisa: {kesempatan}")

if kesempatan == 0:
    print("Kesempatan habis! Game over.")


