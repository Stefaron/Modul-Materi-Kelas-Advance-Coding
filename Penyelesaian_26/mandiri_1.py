stok_barang = {"Laptop", "Printer", "Scanner"}

# Hapus "Monitor" tanpa menyebabkan error
stok_barang.discard("Monitor")
print("Stok barang setelah penghapusan:", stok_barang)  # Output: {'Laptop', 'Printer', 'Scanner'}

