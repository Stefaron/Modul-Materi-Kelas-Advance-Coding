def fungsi_rekursif(parameter):
    # Base case
    if kondisi_berhenti:
        return nilai_akhir
    else:
        # Recursive case
        return fungsi_rekursif(input_yang_dikurangi)

def faktorial(n):
    # Base case
    if n == 1:
        return 1
    # Recursive case
    else:
        return n * faktorial(n - 1)

print(faktorial(5))  # Output: 120

def fibonacci(n):
    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8

def pangkat(x, n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    else:
        return x * pangkat(x, n - 1)

print(pangkat(2, 3))  # Output: 8

def jumlah_list(data):
    # Base case
    if len(data) == 0:
        return 0
    # Recursive case
    else:
        return data[0] + jumlah_list(data[1:])

print(jumlah_list([1, 2, 3, 4, 5]))  # Output: 15

def balik_string(s):
    # Base case
    if len(s) == 0:
        return s
    # Recursive case
    else:
        return balik_string(s[1:]) + s[0]

print(balik_string("hello"))  # Output: "olleh"

