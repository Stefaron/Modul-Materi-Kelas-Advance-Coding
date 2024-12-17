def gabung_string(words):
    sentence = " ".join(words)
    return sentence

kata_1 = input("Masukkan kata pertama : ") # Input: Saya
kata_2 = input("Masukkan kata kedua : ") # Input: Makan
kata_3 = input("Masukkan kata ketiga : ") # Input: Nasi
print(gabung_string([kata_1, kata_2, kata_3]))
#Output : Saya Makan Nasi

