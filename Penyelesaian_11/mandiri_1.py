def hitung_waktu_balapan(kecepatan, panjang_arena):
    # Validasi input
    if kecepatan > 100:
        return "\nKecepatan tidak boleh lebih dari 100 km/detik."
    if panjang_arena < 500:
        return "\nPanjang arena tidak boleh kurang dari 500 km."
    
    # Menghitung waktu untuk 1 putaran
    waktu_per_putaran = panjang_arena / kecepatan
    
    # Menghitung total waktu untuk 5 putaran
    total_waktu = waktu_per_putaran * 5
    
    return f"Waktu total untuk menyelesaikan 5 putaran: {total_waktu} detik"

# Contoh penggunaan
kecepatan = float(input("Masukkan kecepatan mobil (km/detik): "))
panjang_arena = float(input("Masukkan panjang arena balapan (km): "))

print(hitung_waktu_balapan(kecepatan, panjang_arena))

