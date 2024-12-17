# import random

# angka_rahasia = random.randint(1, 10)
# tebakan = None

# while tebakan != angka_rahasia:
#     tebakan = int(input("Tebak angka antara 1 dan 10: "))
#     if tebakan < angka_rahasia:
#         print("Terlalu rendah!")
#     elif tebakan > angka_rahasia:
#         print("Terlalu tinggi!")
#     else:
#         print("Selamat! Tebakanmu benar.")

for angka in range(1, 11):
    if angka == 5:
        print("Angka 5 ditemukan! Berhenti.")
        break
    print("Angka saat ini:", angka)

