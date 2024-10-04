a = int(input("Masukan Sisi A : "))
b = int(input("Masukan Sisi B : "))
c = int(input("Masukan Sisi C : "))

def jenis_segitiga(a, b, c) :
    if a + b > c and a + c > b and b + c > a :
        if a ** 2 + b ** 2 == c ** 2  :
            return "Segitiga-Siku-Siku"
        elif a == b or b == c or a == c :
            return "segita sama Sisi"
        else : 
            return "segitiga sembarang"
    else :
        return "tidak dapat membentuk segitiga"

try:
    hasil = jenis_segitiga(a, b, c)
    print("Jenis Segitiga : " ,hasil)

except ValueError:
    print("Masukkan nilai yang valid untuk panjang sisi.")