skor = {'dio': 120, 'rara': 150, 'udin': 200}
nama = (input("Masukin nama pemain: ")).lower()
if nama in skor:
    print(f"Skor {nama}: {skor[nama]}")
else:
    print(f"{nama} belum main game.")

