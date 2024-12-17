import re

text = "Hari ini cuaca cerah, dan besok mungkin akan hujan."
pattern = r"cuaca"

# Mencari keberadaan pola "cuaca" dalam teks
match = re.search(pattern, text)

if match:
    print("Ketemu! Pola ditemukan di posisi:", match.start())
else:
    print("Pola tidak ditemukan.")

text = "Python adalah bahasa pemrograman yang hebat."
pattern = r"Python"

# Mencari apakah string diawali dengan "Python"
match = re.match(pattern, text)

if match:
    print("Diawali dengan 'Python'!")
else:
    print("Tidak diawali dengan 'Python'.")


text = "Email saya adalah user1@example.com, dan email cadangan adalah user2@domain.org."
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Menemukan semua email dalam teks
emails = re.findall(pattern, text)
print("Email yang ditemukan:", emails)


text = "Kode pos saya adalah 12345 dan kode pos teman saya 67890."
pattern = r"\d{5}"

# Menemukan semua kode pos (5 digit angka) dalam teks
matches = re.finditer(pattern, text)

for match in matches:
    print("Kode pos ditemukan:", match.group(), "- Posisi:", match.start(), "sampai", match.end())


text = "Nomor telepon saya adalah 081234567890."
pattern = r"\d{4}-\d{4}-\d{4}"

# Mengubah format nomor telepon
formatted_text = re.sub(r"(\d{4})(\d{4})(\d{4})", r"\1-\2-\3", text)
print("Nomor telepon dengan format baru:", formatted_text)


text = "Ini kalimat satu. Ini kalimat dua! Ini kalimat tiga?"
pattern = r"[.!?]"

# Membagi teks berdasarkan titik, tanda seru, atau tanda tanya
sentences = re.split(pattern, text)
print("Daftar kalimat:", sentences)

