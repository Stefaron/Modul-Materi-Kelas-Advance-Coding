import re

def validasi_nomor(nomor):
    pattern = r"^\d{4}-\d{4}-\d{4}$"
    return re.match(pattern, nomor) is not None

print(validasi_nomor("0812-3456-7890"))  # Output: True
print(validasi_nomor("081234567890"))    # Output: False

