# # Outer loop untuk baris
# for i in range(5):  # Mengulang sebanyak 5 baris
#     # Inner loop untuk mencetak bintang di setiap baris
#     for j in range(5):  # Setiap baris berisi 5 bintang
#         print("*", end="")  # Mencetak bintang tanpa pindah baris
#     print()  # Pindah ke baris baru setelah inner loop selesai


# Outer loop untuk baris
for i in range(3):
    # Inner loop untuk kolom
    for j in range(3):
        print("#", end=" ")
    print()  # Pindah ke baris baru


