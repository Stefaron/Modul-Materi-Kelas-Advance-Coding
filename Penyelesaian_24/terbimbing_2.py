rute_waktu = {
    ("Kota A", "Kota B"): 120,
    ("Kota A", "Kota C"): 55,
    ("Kota B", "Kota D"): 130,
    ("Kota C", "Kota D"): 45
}

lama_rute = {}
for rute, waktu in rute_waktu.items():
    if waktu > 60:
        lama_rute[rute] = waktu

print("Rute yang memakan waktu lebih dari satu jam:", lama_rute)

