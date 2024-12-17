import re

text = "Ini Adalah Sebuah Contoh Teks."
pattern = r"\b[A-Z][a-z]*\b"

# Temukan kata yang dimulai huruf kapital
result = re.findall(pattern, text)
print("Kata ditemukan:", result)

