import re

def validasi_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$"
    return re.match(pattern, email) is not None

print(validasi_email("user@example.com"))    # Output: True
print(validasi_email("user@domain"))         # Output: False

import re

def validasi_telepon(nomor):
    pattern = r"^\+62\s\d{3}-\d{4}-\d{4}$"
    return re.match(pattern, nomor) is not None

print(validasi_telepon("+62 812-3456-7890"))  # Output: True
print(validasi_telepon("0812-3456-7890"))      # Output: False

import re

text = "Saya sedang belajar Python dan bahasa Python sangat menarik."
pattern = r"\bPython\b"
result = re.findall(pattern, text)

print("Ditemukan kata:", result)

