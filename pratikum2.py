#import math    NO 1

#a = int(input("Masukkan bilangan bulat a: "))
#b = int(input("Masukkan bilangan bulat b: "))  

#jumlah = a + b
#selisih = b - a
#kali = a * b
#sisa_pembagian = a % b
#pembagian = a / b
#log = math.log10(a)
#pangkat = a ** b

#print(f"jumlah a dan b: {jumlah}")
#print(f"selisih b dan a: {selisih}")
#print(f"hasil kali a dan b: {kali}")
#print(f"sisa pembagian a dengan b: {sisa_pembagian}")
#print(f"pembagian a dengan b: {pembagian}")
#print(f"hasil dari  log(a): {log}")
#print(f"a pangkat b: {pangkat}")

import math     #NO 2

Lintang1 = math.radians(float(input("Lintang Kota 1 : ")))
Bujur1 = math.radians(float(input("Bujur Kota 1 : ")))
Lintang2 = math.radians(float(input("Lintang kota 2 : ")))
Bujur2 = math.radians(float(input("Bujur kota 2 : ")))

R = 6371
Lat = Lintang2 - Lintang1
Long = Bujur2 - Bujur1

a = math.sin(Lat/2)*2 + math.cos(Lintang1) * math.cos(Lintang2) * math.sin(Long/2)*2
C3 = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
d = R * C3

print("jarak antara dua titik tersebut adalah ", d, "kilometer")



