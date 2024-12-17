def hitung_kata_terpanjang(text):
    words = text.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

print(hitung_kata_terpanjang("ini adalah kalimat yang cukup panjang"))
# Output: "kalimat"

