def hitung_vokal(text):
    vokal = "aiueo"
    count = 0
    for char in text.lower():
        if char in vokal:
            count += 1
    return count

kalimat = input("Masukkan kalimat: ") # input: Python is fun!!
print(hitung_vokal(kalimat))
# Output: 3

