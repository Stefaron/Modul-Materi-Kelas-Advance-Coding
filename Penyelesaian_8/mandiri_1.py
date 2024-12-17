total_kue = 0
for rak in range(1, 5):  # Ada 4 rak
    print(f"Rak {rak}:")
    for jenis_kue in range(1, 4):  # Setiap rak punya 3 jenis kue
        print(f"Jenis kue {jenis_kue} ada di rak {rak}")
        total_kue += 1
print(f"Total kue: {total_kue}")