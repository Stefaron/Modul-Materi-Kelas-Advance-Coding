def ganti_vokal(s):
    ganti = "a"
    hasil = ""
    for char in s:
        if char in ganti:
            hasil += "*"
        else:
            hasil += char
    return hasil

# Contoh penggunaan
input_string = input("Masukkan sebuah string: ")
print("String setelah penggantian vokal:", ganti_vokal(input_string))