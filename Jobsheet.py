#PROGRAM MENGHITUNG LUAS DAN KELILING BANGUN DATAR

from IPython.display import clear_output

def cls() :
    clear_output(True)

while True:
    #MenuPilihan
    print("Pilihan Program")
    print("1. Luas Persegi")
    print("2. Luas Persegi Panjang")
    print("3. Luas Segitiga")
    print("4. Luas Lingkaran")
    print("5. Keliling Persegi")
    print("6. Keliling Persegi Panjang")
    print("7. Keliling Segitiga")
    print("8. Keliling Lingkaran")
    print("9. Exit")
        
    #input
    pilih = int(input("Masukkan pilihan :"))
    
    cls()

    if pilih == 1:
        print("Menghitung Luas Persegi")
        sisi = int(input("Masukkan Panjang Sisi :"))
        luas = sisi * sisi
        kel = 4 * sisi
        print("Luas Persegi adalah", luas)
     
    else
