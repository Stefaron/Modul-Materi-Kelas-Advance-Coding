def hitung_panjang(s):
    count = 0
    for char in s:
        count += 1
    return count

# Contoh penggunaan
input_string = input("Masukkan sebuah string: ")
print("Panjang string:", hitung_panjang(input_string))
