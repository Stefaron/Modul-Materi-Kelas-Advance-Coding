hp_monster = 30
print(f"HP Monster awal: {hp_monster}")

while hp_monster > 0:
    serang = int(input("Kamu menyerang monster sebanyak : "))
    hp_monster -= serang  # Setiap serangan mengurangi 5 HP
    print(f"HP Monster: {hp_monster}")
    print("Kamu menyerang monster!")

print("Monster kalah! Kamu menang!")
