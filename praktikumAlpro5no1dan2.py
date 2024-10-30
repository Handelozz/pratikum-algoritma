

#value_num = 0
#jumlah_rata = 0

#while True :

    #nilai = input("Masukan Nilai : ")
    #nilai = nilai.upper()

    #if(nilai == '') :
        #print("bentar ya di itung dulu")
        #break
    #elif(nilai == 'A' ) :
        #value_num += 4.00
        #jumlah_rata += 1
        #print(f"Nilai = 4.00")
    #elif(nilai == 'A-' ) :
        #value_num += 3.75
        #jumlah_rata += 1
        #print(f"Nilai = 3.75")
    #elif(nilai == 'B+' ) :
        #value_num += 3.50
        #jumlah_rata += 1
        #print(f"Nilai = 3.50")
    #elif(nilai == 'B' ) :
        #value_num += 3.00
        #jumlah_rata += 1
        #print(f"Nilai = 3.00")
    #elif(nilai == 'B-' ) :
        #value_num += 2.75
        #jumlah_rata += 1
        #print(f"Nilai = 2.75")
    #elif(nilai == 'C+' ) :
        #value_num += 2.50
        #jumlah_rata += 1
        #print(f"Nilai = 2.50")
    #elif(nilai == 'C' ) :
        #value_num += 2.00
        #jumlah_rata += 1
        #print(f"Nilai = 2.00")
    #elif(nilai == 'C-' ) :
        #value_num += 1.75
        #jumlah_rata += 1
       # print(f"Nilai = 1.75")
    #elif(nilai == 'D' ) :
        #value_num += 1.50
        #jumlah_rata += 1
        #print(f"Nilai = 1.50")
    #elif(nilai == 'E' ) :
        #value_num += 1.25
        #jumlah_rata += 1
        #print(f"Nilai = 1.25")
    #else :
        #print("Nilai yang anda masukan tidak valid,Masukan lagi")
    
#if value_num == 0 :
    #print("Tidak ada nilai yang dapat dihitung")
    
#rata_rata = value_num / jumlah_rata
#print(f"rata-rata nilai : {rata_rata}")



#NO 2

def hitung_tiket():
    total_harga = 0

    print("Masukkan umur untuk setiap pengunjung. Ketik 'selesai' jika sudah selesai memasukkan data.\n")

    while True:
        umur_input = input("Masukkan umur pengunjung: ")

        # Memeriksa apakah input adalah perintah 'selesai'
        if umur_input.lower() == 'selesai':
            break

        try:
            umur = int(umur_input)

            # Menentukan harga tiket berdasarkan umur
            if umur <= 2:
                harga = 0
            elif 3 <= umur <= 12:
                harga = 14
            elif umur >= 65:
                harga = 18
            else:
                harga = 23

            total_harga += harga
            print(f"Harga tiket untuk umur {umur} tahun adalah ${harga}\n")

        except ValueError:
            print("Umur tidak valid. Harap masukkan angka yang benar.\n")

    print(f"Total harga tiket untuk semua pengunjung adalah ${total_harga}")

    # Memasukkan pembayaran
    try:
        pembayaran = float(input("Masukkan jumlah uang yang dibayarkan: $"))

        if pembayaran < total_harga:
            print("Uang tidak cukup. Harap bayar dengan jumlah yang sesuai.")
        else:
            kembalian = pembayaran - total_harga
            print(f"Kembalian Anda: ${kembalian:.2f}")

    except ValueError:
        print("Jumlah uang tidak valid. Harap masukkan angka yang benar.")

# Memanggil fungsi untuk menjalankan program
hitung_tiket()