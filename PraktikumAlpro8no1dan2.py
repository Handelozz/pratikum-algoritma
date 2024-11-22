#def penjumlahan_rekursif(angka_list, index=0):
    #if index == len(angka_list):
        #return 0
    #else:
        #return angka_list[index] + penjumlahan_rekursif(angka_list, index + 1)

#jumlah = int(input("Masukkan Jumlah: "))
#angka_list = []

#for i in range(jumlah):
    #angka = int(input(f"Masukkan angka ke-{i+1}: "))
    #angka_list.append(angka)

#hasil = penjumlahan_rekursif(angka_list)
#print("Hasil dari penjumlahan adalah:", hasil)

#NO 2

def pangkat_rekursif(angka, pangkat):
    if pangkat == 0: 
        return 1
    elif pangkat > 0:  
        return angka ** pangkat
    else:  
        return 1 / pangkat_rekursif(angka, -pangkat)

angka = input("Angka: ")
if angka == '':
    print("bye") 
else:
    angka = float(angka)
    pangkat = int(input("Pangkat: "))
    hasil = pangkat_rekursif(angka, pangkat)
    print(hasil)