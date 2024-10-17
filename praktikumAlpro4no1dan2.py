#n = int(input("Masukkan nilai: "))

#for i in range(n, 0, -1):
    #print(str(i) * i)


def jumlah_hari (tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

while True:
    bulan = int(input("Masukkan bulan (1-12): "))
    tahun = int(input("Masukkan tahun: "))

    if bulan == 2:
        if jumlah_hari (tahun):
            print("Jumlah hari: 29")
        else:
            print("Jumlah hari: 28")
    elif bulan in [4, 6, 9, 11]:
        print("Jumlah hari: 30")
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        print("Jumlah hari: 31")
    else:
        print("Bulan tidak valid.")


