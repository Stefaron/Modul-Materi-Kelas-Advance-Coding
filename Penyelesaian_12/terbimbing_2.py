hitung_kecepatan = lambda jarak, waktu: "Kecepatan terlalu tinggi!" if (jarak / waktu) > 120 else jarak / waktu

# Contoh penggunaan
print(hitung_kecepatan(500, 3))  # Output: Kecepatan terlalu tinggi!
print(hitung_kecepatan(500, 5))  # Output: 100.0
