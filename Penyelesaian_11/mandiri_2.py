def hitung_total_waktu(panjang_arena, kecepatan, jumlah_putaran):
    # Menghitung jarak total yang harus ditempuh
    total_jarak = panjang_arena * jumlah_putaran
    
    # Menghitung total waktu
    total_waktu = total_jarak / kecepatan
    
    return total_waktu

# Contoh penggunaan
panjang_arena = float(input("Masukkan panjang arena (km): "))
kecepatan = float(input("Masukkan kecepatan mobil (km/detik): "))
jumlah_putaran = int(input("Masukkan jumlah putaran: "))

waktu_total = hitung_total_waktu(panjang_arena, kecepatan, jumlah_putaran)
print("Total waktu yang diperlukan: ", waktu_total, "detik")
