def hitung_awalan(text, letter):
    words = text.split()
    count = 0
    for word in words:
        if word.startswith(letter):
            count += 1
    return count

kalimat = input("Masukkan kalimat: ") # input: belajar dan bermain
kata_dicari = input("Masukkan huruf depan kata yang ingin dicari: ") # input: b
print(hitung_awalan(kalimat, kata_dicari))
# Output: 2


