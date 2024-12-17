def perkalian(x, y):
    # Base case
    if y == 0:
        return 0
    # Recursive case
    else:
        return x + perkalian(x, y - 1)

print(perkalian(3, 4))  # Output: 12

