buah = {"apel", "jeruk", "mangga"}
for item in buah:
    print(item)

buah = {"apel", "jeruk", "mangga"}

print("apel" in buah)  # Output: True
print("pisang" in buah)  # Output: False

angka = {1, 2, 3, 4, 5}
print(len(angka))  # Output: 5

buah = {"apel", "jeruk"}
print(buah) # Output: {"apel", "jeruk"}
buah.add("mangga")
print(buah)  # Output: {"apel", "jeruk", "mangga"}

buah.add("apel")
print(buah)  # Output: {"apel", "jeruk", "mangga"} (apel nggak ditambahin lagi)

buah = {"apel", "jeruk", "mangga"}
buah.remove("jeruk")
print(buah)  # Output: {"apel", "mangga"}

# Coba hapus elemen yang nggak ada di set
# buah.remove("pisang")  # Ini bakal error KeyError karena "pisang" nggak ada

buah = {"apel", "jeruk", "mangga"}
buah.discard("jeruk")
print(buah)  # Output: {"apel", "mangga"}

# Coba hapus elemen yang nggak ada di set
buah.discard("pisang")  # Nggak error meski "pisang" nggak ada
print(buah)  # Output tetap {"apel", "mangga"}

buah = {"apel", "jeruk", "mangga"}
item_dihapus = buah.pop()
print(f"Item yang dihapus: {item_dihapus}")
print(f"Set setelah pop: {buah}")

buah = {"apel", "jeruk", "mangga"}
buah.clear()
print(buah)  # Output: set()

