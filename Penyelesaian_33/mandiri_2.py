import re

text = "Kalimat satu. Kalimat dua! Kalimat tiga?"
pattern = r"[.!?]"

kalimat = re.split(pattern, text)
print("Daftar kalimat:", kalimat)
