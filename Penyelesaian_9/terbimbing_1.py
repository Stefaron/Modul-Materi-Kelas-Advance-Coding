# Jawaban:
total = 0
angka = 0

while angka >= 0:
    angka = int(input("Masukkan angka (masukkan angka negatif untuk berhenti): "))
    if angka >= 0:
        total += angka

print(f"Total semua angka yang dimasukkan: {total}")
