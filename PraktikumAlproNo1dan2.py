

#def rata_rata_nilai():
    #total_nilai = 0
    #jumlah_nilai = 0

    #while True:
        #nilai = input("Masukkan Nilai : ").strip()
        #nilai = nilai.upper()
        
        #if nilai == '':
            #break
        #elif nilai == 'A':
            #total_nilai += 4.00
            #jumlah_nilai += 1
            #print("Nilai = 4.00")
        #elif nilai == 'A-':
            #total_nilai += 3.75
            #jumlah_nilai += 1
            #print("Nilai = 3.75")
        #elif nilai == 'B+':
            #total_nilai += 3.50
            #jumlah_nilai += 1
            #print("Nilai = 3.50")
        #elif nilai == 'B':
            #total_nilai += 3.00
            #jumlah_nilai += 1
            #print("Nilai = 3.00")
        #elif nilai == 'B-':
            #total_nilai += 2.75
            #jumlah_nilai += 1
            #print("Nilai = 2.75")
        #elif nilai == 'C+':
            #total_nilai += 2.50
            #jumlah_nilai += 1
            #print("Nilai = 2.50")
        #elif nilai == 'C':
            #total_nilai += 2.00
            #jumlah_nilai += 1
            #print("Nilai = 2.00")
        #elif nilai == 'C-':
            #total_nilai += 1.75
            #jumlah_nilai += 1
            #print("Nilai = 1.75")
        #elif nilai == 'D':
            #total_nilai += 1.50
            #jumlah_nilai += 1
            #print("Nilai = 1.50")
        #elif nilai == 'E':
            #total_nilai += 1.25
            #jumlah_nilai += 1
            #print("Nilai = 1.25")
        #else:
            #print(f"Kategori '{nilai}' tidak valid. Silakan coba lagi.")

    #if jumlah_nilai == 0:
        #print("Tidak ada nilai valid untuk dihitung.")
        #return

    #rata_rata = total_nilai / jumlah_nilai
    #print(f"Rata-rata nilai: {rata_rata:.2f}")

#rata_rata_nilai()

#NO 2

def is_kabisat(tahun):
   """Mengembalikan True jika tahun adalah tahun kabisat, False jika bukan."""
   return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

def jumlah_hari_dalam_bulan(bulan, tahun):
  """Mengembalikan jumlah hari dalam suatu bulan, dengan mempertimbangkan tahun kabisat."""
  bulan_31 = [1, 3, 5, 7, 8, 10, 12]
  bulan_30 = [4, 6, 9, 11]

  if bulan in bulan_31:
    return 31
  elif bulan in bulan_30:
    return 30
  elif bulan == 2:
    if is_kabisat(tahun):
      return 29
    else:
      return 28
  else:
    return "Bulan tidak valid"

# Input pengguna
bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

# Panggil fungsi dan tampilkan hasil
jumlah_hari = jumlah_hari_dalam_bulan(bulan, tahun)
print("Jumlah hari dalam bulan", bulan, "tahun", tahun, "adalah", jumlah_hari)