nilai_kelas = {'Budi': 75,
               'Susi': 80,
               'Doni': 60,
               'Nani': 65,
               'Dono': 70,
               'Vivi': 85}

for nama, nilai in nilai_kelas.items():
    if nilai < 70:
        print(f"{nama} perlu remedial dengan nilai {nilai}")


