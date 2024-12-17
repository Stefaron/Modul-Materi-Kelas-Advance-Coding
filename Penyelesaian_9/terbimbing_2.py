# Jawaban:
jawaban_benar = 3  # Angka yang harus ditebak
tebakan = int(input("Tebak angka dari 1 hingga 5: "))

while tebakan != jawaban_benar:
    tebakan = int(input("Salah! Coba lagi, tebak angka dari 1 hingga 5: "))

print("Selamat! Tebakan kamu benar.")


