nilai1 = int(input("Masukkan nilai mata pelajaran 1: "))
nilai2 = int(input("Masukkan nilai mata pelajaran 2: "))
nilai3 = int(input("Masukkan nilai mata pelajaran 3: "))

rata_rata = (nilai1 + nilai2 + nilai3) / 3

if rata_rata > 85:
    print("Nilai A")
elif 70 <= rata_rata <= 85:
    print("Nilai B")
elif 50 <= rata_rata < 70:
    print("Nilai C")
else:
    print("Nilai D")
    