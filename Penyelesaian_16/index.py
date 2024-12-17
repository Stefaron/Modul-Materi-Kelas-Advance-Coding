text = "Hello, World!"

# Mengambil substring dari indeks 0 sampai 5
print(text[0:5])     # Output: Hello

# Mengambil substring dari indeks 7 hingga akhir
print(text[7:])      # Output: World!

# Mengambil setiap karakter kedua dari indeks 0 hingga akhir
print(text[::2])     # Output: Hlo ol!

text = "hello world"
print(text.capitalize())  # Output: Hello world

text = "Pagi yang cerah"
print(text.count("a"))  # Output: 3

text = "Saya belajar di REC"
print(text.endswith("REC"))  # Output: True

text = "Hari ini saya makan sop"
print(text.startswith("sop"))  # Output: False

text = "hello world"
print(text.find("world"))  # Output: 6

text = "soto sapi"
print(text.islower())  # Output: True

text = "ROBOTIC Education"
print(text.isupper())  # Output: False

text = "12345"
print(text.isdigit())  # Output: True

text = "   ini contoh    "
print(text.strip())  # Output: "ini contoh"

text = "Python is fun"
print(text.split())  # Output: ['Python', 'is', 'fun']

