belanja = ["apel", "pisang"]
belanja.append("jeruk")
print(belanja)  # Output: ["apel", "pisang", "jeruk"]

belanja = ["apel", "pisang"]
belanja.insert(1, "mangga")
print(belanja)  # Output: ["apel", "mangga", "pisang"]

belanja = ["apel", "pisang", "jeruk"]
belanja.remove("pisang")
print(belanja)  # Output: ["apel", "jeruk"]


belanja = ["apel", "pisang", "jeruk", "mangga"]

buah = belanja.pop()  # ambil "mangga"
print(buah)  # Output: "mangga"
print(belanja)  # Output: ["apel", "pisang", "jeruk"]

buah = belanja.pop(1) # ambil "pisang"
print(buah) # Output: "pisang"
print(belanja) # Output: ['apel', 'jeruk']

belanja = ["apel", "pisang", "apel", "jeruk"]
print(belanja.count("apel"))  # Output: 2

belanja = ["apel", "pisang", "jeruk"]
print(belanja.index("jeruk"))  # Output: 2

angka = [3, 1, 2]
angka.sort()
print(angka)  # Output: [1, 2, 3]

angka.sort(reverse=True)
print(angka)  # Output: [3, 2, 1]

belanja = ["apel", "pisang", "jeruk"]
belanja.reverse()
print(belanja)  # Output: ["jeruk", "pisang", "apel"]

belanja = ["apel", "pisang", "jeruk"]
print(len(belanja))  # Output: 3

angka = [1, 2, 3]
print(sum(angka))  # Output: 6

# Contoh list dengan berbagai tipe data
data = [1, "apel", [2, 3]]

# Contoh string (isi karakter aja)
kata = "Hello, World!"

# Contoh mengubah elemen di list
data = ["apel", "pisang"]
data[0] = "jeruk"
print(data)  # Output: ["jeruk", "pisang"]

# Contoh mencoba mengubah elemen di string (ini bakal error)
kata = "halo"
kata[0] = "j"  # Error!

# Akses elemen di list
data = ["apel", "pisang", "jeruk"]
print(data[1])  # Output: "pisang"

# Akses elemen di string
kata = "hello"
print(kata[1])  # Output: "e"

    