karyawan = {
    "Andi": {"gaji": 8000000, "divisi": "IT"},
    "Budi": {"gaji": 7000000, "divisi": "Marketing"},
    "Cici": {"gaji": 6000000, "divisi": "Finance"}
}

# Menampilkan nama, gaji, dan divisi
for nama, info in karyawan.items():
    gaji, divisi = info["gaji"], info["divisi"]
    print(f"Karyawan: {nama}, Gaji: {gaji}, Divisi: {divisi}")
