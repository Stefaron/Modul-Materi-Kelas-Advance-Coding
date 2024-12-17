kalimat = "data adalah ilmu yang penting dalam dunia modern"
kata_list = kalimat.split()

cari_panjang = int(input("Saya mencari kata yang berjumlah: "))

# Mengelompokkan kata berdasarkan panjangnya
panjang_kata = []
for kata in kata_list:
    panjang = len(kata)
    if panjang == cari_panjang:
        panjang_kata.append(kata)

print("Kata berdasarkan panjang yang anda cari:", panjang_kata)

