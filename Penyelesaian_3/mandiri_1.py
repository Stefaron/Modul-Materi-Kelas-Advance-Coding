# Total uang yang dimiliki
total_uang = 200000

# Pecahan 50.000 yang dimiliki
pecahan_50k = total_uang // 50000

# Menghitung jumlah lembar pecahan 20.000
pecahan_20k = total_uang // 20000

# Menghitung sisa uang setelah ditukar menjadi pecahan 20.000
sisa_uang = total_uang % 20000

# Menghitung jumlah lembar pecahan 10.000 dari sisa uang
pecahan_10k = sisa_uang // 10000

# Mencetak hasil penukaran
print("Ibu memiliki", pecahan_50k, "lembar pecahan Rp50.000")
print("Ibu mendapatkan", pecahan_20k, "lembar pecahan Rp20.000 dan", pecahan_10k, "lembar pecahan Rp10.000")