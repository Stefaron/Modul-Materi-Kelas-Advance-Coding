persiapan_pesta = {
    "Gelas": 50,
    "Piring": 30,
    "Sendok": 20
}

def tambah_item(item, jumlah):
    if item in persiapan_pesta:
        persiapan_pesta[item] += jumlah
        print(f"{jumlah} {item} berhasil ditambah!")
    else:
        persiapan_pesta[item] = jumlah
        print(f"{item} berhasil ditambahkan!")

tambah_item("Gelas", 10)
print(persiapan_pesta)
