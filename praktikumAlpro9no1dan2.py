
#def tulis_biodata():

    #with open("Biodata.txt", "w") as file:

        #nama = input("Nama: ")
        #umur = input("Umur: ")
        #alamat = input("Alamat: ")
        #email = input("Email: ")
        #dosen_wali = input("Dosen Wali: ")

        #file.write("Nama: " + nama + "\n")
        #file.write("Umur: " + umur + "\n")
        #file.write("Alamat: " + alamat + "\n")
        #file.write("Email: " + email + "\n")
        #file.write("Dosen Wali: " + dosen_wali + "\n")

    #print("Biodata telah berhasil disimpan dalam Biodata.txt")

#def baca_biodata():
    #try:

        #with open("Biodata.txt", "r") as file:

            #print("\nBerikut ini data kamu:")
            #print(file.read())
    #except FileNotFoundError:
        #print("File Biodata.txt tidak ditemukan. Pastikan file sudah ada.")

#tulis_biodata() 
#baca_biodata()  

#NO 2

def read_file():
    filename = input("masukan nama file: ").strip()
    name = input("masukan nama anda: ").strip()
    nim = input("masukan NIM an anda ").strip()
    year = input("masukan tahun angkatan ").strip()

    file_content = (
        f"Informasi pwngguna\n"
        f"nama file     : {filename}\n"
        f"nama anda     : {name}\n"
        f"NIM anda      : {nim}\n"

    )

    try:
        with open(filename, "w") as file:
            file.write(file_content)
        print(f"\nfile '{filename}' berhasil dibuat!\n")
    except Exception as e:
        print(f"\nTerjadi kesalahan saat membuat file: {e}\n")


def read_file():
    filename = input("masukan nama file: ").strip()
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"\n isi file '{filename}' \n{content}\n")
    except FileNotFoundError:
            print(f"\n isi file '{filename}' \n{content}\n")
    except Exception as e:
            print(f"\nterjadi kesalahan saat membaca file: {e}\n")


def append_to_file():
    filename = input("masukan nama file:").strip()
    name = input("masukan nama sahabat").strip()
    note = input("masukan catatan sahabat").strip()

    file_content = (
         f"tambahan informasi\n"
         f"nama sahabat    : {name}\n"
         f"catatan         : {note}\n"
         
           )

    try:
         with open(filename, "a") as file:
              file.write(file_content)
         print("\nteks berhasil ditambahkan ke file '{filename}'.\n")
    except Exception as e:
         print(f"\nterjadi kesalahan saat menambahkan teks ke file: {e}\n")

def main():
     while True:
          print("\n========== menu file handling ==========")
          print("1. buat file baru")
          print("2. baca file")
          print("3. tambah teks ke file")
          print("4. keluar")
          print("========================================")

          choice = input("pilih menu (1/2/3/4): ").strip()

          if choice == "1":
               create_file()
          elif choice == "2":
               read_file()
          elif choice == "3":
               append_to_file()
          elif choice == "4":
               print("\nterima kasih telah menggunakan program ini. Bye Bye! :)")
               break
          else:
               print("\npilihan tidak valid.silakan coba lagi.\n")

main()