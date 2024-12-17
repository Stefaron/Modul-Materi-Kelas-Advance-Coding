mata_pelajaran = {"Matematika", "Fisika", "Kimia", "Biologi"}

cek_mapel = input("Masukkan mapel yang ingin anda cari: ").capitalize()

# Cek keberadaan "Bahasa Inggris"
if cek_mapel not in mata_pelajaran:
    mata_pelajaran.add(cek_mapel)

# Hitung jumlah total mata pelajaran
jumlah_pelajaran = len(mata_pelajaran)
print("Mata pelajaran:", mata_pelajaran)
print("Jumlah mata pelajaran:", jumlah_pelajaran)

