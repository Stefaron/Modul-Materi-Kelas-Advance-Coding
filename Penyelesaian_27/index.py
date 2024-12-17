setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

# Menggunakan metode union()
gabungan = setA.union(setB)
print(gabungan)  # Output: {1, 2, 3, 4, 5, 6}

# Menggunakan operator |
gabungan_operator = setA | setB
print(gabungan_operator)  # Output: {1, 2, 3, 4, 5, 6}

setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

# Menggunakan metode intersection()
irisan = setA.intersection(setB)
print(irisan)  # Output: {3, 4}

# Menggunakan operator &
irisan_operator = setA & setB
print(irisan_operator)  # Output: {3, 4}

setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

# Menggunakan metode difference()
selisih = setA.difference(setB)
print(selisih)  # Output: {1, 2}

# Menggunakan operator -
selisih_operator = setA - setB
print(selisih_operator)  # Output: {1, 2}

setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

# Menggunakan metode symmetric_difference()
selisih_simetris = setA.symmetric_difference(setB)
print(selisih_simetris)  # Output: {1, 2, 5, 6}

# Menggunakan operator ^
selisih_simetris_operator = setA ^ setB
print(selisih_simetris_operator)  # Output: {1, 2, 5, 6}

setA = {1, 2}
setB = {1, 2, 3, 4}

# Cek apakah setA adalah subset dari setB
print(setA.issubset(setB))  # Output: True

setA = {1, 2, 3, 4}
setB = {1, 2}

# Cek apakah setA adalah superset dari setB
print(setA.issuperset(setB))  # Output: True

