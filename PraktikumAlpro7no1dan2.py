#import math
#x = False
#n = ""

#def not_prime(n):
    #if n % 2 == 0 and n > 2: 
        #for i in range(3, int(math.sqrt(n)) + 1, 2):
            #if n % i == 0:
                #return False
        #print(n, "bukanlah bilangan Prima")
    #elif n == 1:
        #print("bukanlah bilangan Prima")
    #else:
        #is_prime(n)

#def is_prime(n):
    #print(n, "adalah bilangan Prima")
    
#while (not x):
    #print("Gunakan 0 untuk stop")
    #n = int(input("masukan angka: "))
    #if n == 0:
        #x = True
    #else:
        #not_prime(n)

#NO 2

print("Ketik 0 Untuk Menghentikan Program")
def ordinal_number(angka):
    if 10 <= angka % 100 <= 20:
        ordinal = 'th'  
    else:
        if angka % 10 == 1:
            ordinal = 'st'
        elif angka % 10 == 2:
            ordinal = 'nd'
        elif angka % 10 == 3:
            ordinal = 'rd'
        else:
            ordinal = 'th'
        
    return f"({angka} , '{ordinal}')"

def main():
    while True:
        try:
            user_input = int(input("Masukkan angka: "))
            print(ordinal_number(user_input))
            
            if user_input == 0 :
                print("Terimakasih telah menggunakan program saya")
                break

        except ValueError:
            print("Input tidak valid. Silakan masukkan angka yang benar.")

main()