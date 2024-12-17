komputer_kampus = {
    (101, 1): "Aktif",
    (101, 2): "Tidak Aktif",
    (102, 1): "Aktif",
    (102, 2): "Tidak Aktif",
    (103, 1): "Aktif"
}

komputer_tidak_aktif = []
for k, status in komputer_kampus.items():
    if status == "Tidak Aktif":
        komputer_tidak_aktif.append(k)
        
print("Komputer yang tidak aktif:", komputer_tidak_aktif)

