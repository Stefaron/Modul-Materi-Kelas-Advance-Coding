import re

text = "Ini adalah sebuah pola: abc.def."
pattern = r"abc\.def"

# Mencari pola yang mengandung titik literal
result = re.search(pattern, text)

if result:
    print("Pola ditemukan:", result.group())
else:
    print("Pola tidak ditemukan.")

