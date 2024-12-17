import re

text = "Python adalah bahasa pemrograman yang sangat populer. Python digunakan untuk machine learning, web development, dan lain-lain."
pattern = r"populer"

# Mencari kata "populer" pertama kali
result = re.search(pattern, text)

if result:
    print(f"Kata {pattern} ditemukan di posisi:", result.start())
else:
    print(f"Kata {pattern} tidak ditemukan.")

