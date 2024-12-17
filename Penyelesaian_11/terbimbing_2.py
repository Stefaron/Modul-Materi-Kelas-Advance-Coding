def hitung_kecepatan_minimal(panjang_arena, waktu):
    # Menghitung total jarak yang harus ditempuh
    total_jarak = panjang_arena * 10
    
    # Menghitung kecepatan minimal
    kecepatan_minimal = total_jarak / waktu
    
    print("Kecepatan minimal yang diperlukan: ", kecepatan_minimal, "km/detik")

# Contoh penggunaan
panjang_arena = float(input("Masukkan panjang arena (km): "))
waktu = float(input("Masukkan waktu yang tersedia (detik): "))

hitung_kecepatan_minimal(panjang_arena, waktu)



