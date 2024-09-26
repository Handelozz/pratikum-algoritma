def hitung_luas_ruangan(panjang, lebar):
    return panjang * lebar

panjang = float(input("Masukkan panjang ruangan (meter): "))
lebar = float(input("Masukkan lebar ruangan (meter): "))

luas = hitung_luas_ruangan(panjang, lebar)

print(f"Luas ruangan adalah {luas} meter persegi.")
