import re

text = "Halo! Apa kabar? Bagaimana kabarmu!"
pattern = r"[A-Za-z\s]+!"

# Cari semua kalimat yang diakhiri tanda seru
result = re.findall(pattern, text)
print("Kalimat dengan tanda seru:", result)
