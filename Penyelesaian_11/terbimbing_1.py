def hitung_jarak(kecepatan):
    # Validasi kecepatan
    if kecepatan > 200:
        print("Kecepatan tidak boleh lebih dari 200 km/detik.") 
    
    # Menghitung jarak yang ditempuh dalam 10 detik
    jarak = kecepatan * 10
    
    print("Jarak yang ditempuh dalam 10 detik: ", jarak, "km")

# Contoh penggunaan
kecepatan = float(input("Masukkan kecepatan mobil (km/detik): "))
hitung_jarak(kecepatan)


