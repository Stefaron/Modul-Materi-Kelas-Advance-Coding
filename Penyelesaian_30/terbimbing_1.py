def jumlah_angka(n):
    # Base case
    if n == 1:
        return 1
    # Recursive case
    else:
        return n + jumlah_angka(n - 1)

print(jumlah_angka(5))  # Output: 15

