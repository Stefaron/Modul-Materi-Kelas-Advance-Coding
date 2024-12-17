jawaban_benar = 7  # Angka rahasia
kesempatan = 3

while kesempatan > 0:
    tebakan = int(input(f"Tebak angka (1-10). Kamu punya {kesempatan} kesempatan: "))
    if tebakan == jawaban_benar:
        print("Selamat! Tebakan kamu benar.")
        break  # Keluar dari loop jika tebakan benar
    else:
        kesempatan -= 1  # Kurangi kesempatan

if kesempatan == 0:
    print("Game over! Kesempatan kamu habis.")



