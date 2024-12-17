def hitung_vokal(s):
    vokal = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vokal:
            count += 1
    return count

# Contoh penggunaan
input_string = input("Masukkan sebuah string: ")
print("Jumlah vokal:", hitung_vokal(input_string))
