# Menerima input gaji pokok dan jumlah jam lembur
gaji_pokok = int(input("Masukkan gaji pokok: Rp "))
jam_lembur = int(input("Masukkan jumlah jam lembur: "))

# Menghitung total gaji
total_gaji = gaji_pokok + (jam_lembur * 20000)

# Mencetak total gaji karyawan
print("Total gaji karyawan adalah Rp", total_gaji)
