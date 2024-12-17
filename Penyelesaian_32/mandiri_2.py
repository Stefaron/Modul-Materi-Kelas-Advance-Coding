import re

text = "123abc456def789ghi"
pattern_angka = r"\d+"
pattern_huruf = r"[a-z]+"

# Temukan angka dan huruf
angka = re.findall(pattern_angka, text)
huruf = re.findall(pattern_huruf, text)

print("Angka:", angka)
print("Huruf:", huruf)
