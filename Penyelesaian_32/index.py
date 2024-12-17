import re

text = "Selamat datang di dunia Python!"
pattern = r"Python"
result = re.search(pattern, text)

if result:
    print("Ketemu!")
else:
    print("Gak ketemu!")

text = "Selamat pagi! Halo semuanya!"
pattern = r"^Selamat.*!"
result = re.search(pattern, text)

if result:
    print("Teks diawali dengan 'Selamat' dan ada tanda seru!")
else:
    print("Tidak ditemukan.")


text = "Lihat versi terbaru di sini: 3.10.1"
pattern = r"\d\.\d{2}\.\d"
result = re.search(pattern, text)

if result:
    print("Versi ditemukan:", result.group())
else:
    print("Versi tidak ditemukan.")

