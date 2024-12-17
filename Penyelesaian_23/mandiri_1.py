parkir_kendaraan = {
    ("B1234ABC", 1): "08:00",
    ("D5678DEF", 2): "09:30",
    ("F9012GHI", 1): "10:15",
    ("B3456JKL", 3): "11:00"
}

lantai_1 = []
for (plat, lantai) , waktu in parkir_kendaraan.items():
    if lantai == 1:
        lantai_1.append(plat)
print("Kendaraan di lantai 1:", lantai_1)

