import math

# Fungsi kalkulator sederhana
def simple_calculator():
    print("\n--- Mode Kalkulator Sederhana ---")
    operation = input("Pilih operasi (tambah, kurang, kali, bagi): ").lower()
    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua: "))

    if operation == "tambah":
        result = num1 + num2
    elif operation == "kurang":
        result = num1 - num2
    elif operation == "kali":
        result = num1 * num2
    elif operation == "bagi":
        if num2 == 0:
            return "Error: Pembagian dengan nol tidak valid."
        result = num1 / num2
    else:
        return "Operasi tidak valid!"

    return f"Hasil: {result}"

# Fungsi kalkulator ilmiah
def scientific_calculator():
    print("\n--- Mode Kalkulator Ilmiah ---")
    operation = input("Pilih operasi (pangkat, akar, logaritma, sin, cos, tan): ").lower()

    if operation == "pangkat":
        base = float(input("Masukkan angka dasar: "))
        exponent = float(input("Masukkan pangkat: "))
        result = math.pow(base, exponent)
    elif operation == "akar":
        num = float(input("Masukkan angka: "))
        if num < 0:
            return "Error: Akar kuadrat dari angka negatif tidak valid."
        result = math.sqrt(num)
    elif operation == "logaritma":
        num = float(input("Masukkan angka: "))
        base = float(input("Masukkan basis: "))
        if num <= 0 or base <= 0:
            return "Error: Logaritma hanya valid untuk angka positif."
        result = math.log(num, base)
    elif operation in ["sin", "cos", "tan"]:
        angle = float(input("Masukkan sudut dalam derajat: "))
        radians = math.radians(angle)
        if operation == "sin":
            result = math.sin(radians)
        elif operation == "cos":
            result = math.cos(radians)
        elif operation == "tan":
            result = math.tan(radians)
    else:
        return "Operasi tidak valid!"

    return f"Hasil: {result}"

# Program utama
print("Selamat datang di Advanced Kalkulator!")
mode = input("Pilih mode (sederhana/ilmiah): ").lower()

if mode == "sederhana":
    print(simple_calculator())
elif mode == "ilmiah":
    print(scientific_calculator())
else:
    print("Mode tidak valid!")
