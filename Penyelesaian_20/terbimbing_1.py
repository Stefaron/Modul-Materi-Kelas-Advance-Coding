def cari_nilai(nama):
    siswa = {'Andi': 80, 'Budi': 90, 'Citra': 75, 'Dina': 85}
    if (nama in siswa):
        return siswa.get(nama)
    else:
        return "Siswa tidak ada"
    

print(cari_nilai("Andi")) # Output: 80
print(cari_nilai("Eva")) # Output: Siswa tidak ada

