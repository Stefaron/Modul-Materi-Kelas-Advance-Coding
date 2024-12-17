# Fungsi buat normalisasi input (biar huruf besar/kecil nggak masalah)
def normalize_name(name):
    return name.strip().lower()

# Fungsi kalkulator uang kembalian
def calculate_change(items, payment):
    # Normalisasi nama makanan
    normalized_items = {}
    for name, price in items:
        norm_name = normalize_name(name)
        if norm_name in normalized_items:
            normalized_items[norm_name] += price
        else:
            normalized_items[norm_name] = price

    # Hitung total harga
    total_price = sum(normalized_items.values())
    
    # Cari makanan termahal
    most_expensive = max(normalized_items.items(), key=lambda x: x[1])

    # Hitung kembalian
    change = payment - total_price
    
    return total_price, change, most_expensive

# Input data makanan dan harga
print("Masukkan nama makanan dan harganya (contoh: Pizza 50000). Ketik 'done' kalau selesai.")
items = []
while True:
    entry = input("> ")
    if entry.lower() == "done":
        break
    try:
        name, price = entry.rsplit(" ", 1)
        price = int(price)
        items.append((name, price))
    except ValueError:
        print("Format salah, coba lagi!")

# Input jumlah uang
payment = int(input("Masukkan jumlah uang yang dibayar: "))

# Hitung hasil
total_price, change, most_expensive = calculate_change(items, payment)

# Output hasil
print("\n--- Hasil Kalkulator Uang Kembalian ---")
print(f"Total Harga: Rp{total_price:,}")
if change < 0:
    print(f"Uang kurang: Rp{abs(change):,}")
else:
    print(f"Kembalian: Rp{change:,}")
print(f"Makanan Termahal: {most_expensive[0].title()}, Rp{most_expensive[1]:,}")
