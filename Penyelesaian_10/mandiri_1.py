angka = 1
total = 0

while angka <= 20:  # Loop sampai angka 20
    if angka % 2 == 0:  # Cek jika angka genap
        total += angka  # Tambahkan angka ke total
    angka += 1

print(f"Jumlah bilangan genap dari 1 sampai 20 adalah: {total}")
