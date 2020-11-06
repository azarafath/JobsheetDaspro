#PROGRAM MENGHITUNG LUAS DAN KELILING BANGUN DATAR
#DIBUAT OLEH AHMAD ZAKARIA FATHONI & FEBRI ARDANA

from IPython.display import clear_output

def cls():
    clear_output(True)
    
def luas_persegi(s):
    luas = s * s
    return luas

def luas_persegi_panjang(p,l):
    luas = p * l
    return luas

def luas_segitiga(a,t):
    luas = a * t
    return luas

def luas_lingkaran(r):
    luas = 3.14 * r * r
    return luas

def keliling_persegi(s):
    keliling = 4 * s
    return keliling

def keliling_persegi_panjang(p,l):
    keliling = 2 * (p + l)
    return keliling

def keliling_segitiga(a,b,c):
    keliling = a + b + c
    return keliling

def keliling_lingkaran(r):
    keliling = 2 * 3.14 * r
    return keliling

while True :
    #Menu Pilihan Bidang
    print("Pilihan Bangun Datar")
    print("1. Luas Persegi")
    print("2. Luas Persegi Panjang")
    print("3. Luas Segitiga")
    print("4. Luas Lingkaran")
    print("5. Kelilins Persegi")
    print("6. Keliling Persegi Panjang")
    print("7. Keliling Segitiga")
    print("8. Keliling Lingkaran")
    print("9. Exit ")
    
    #Input
    pilih = int(input("Masukkan Pilihan :"))

    cls()

    if pilih == 1:
        print("Menghitung Luas Persegi")
        s = int(input("Masukkan panjang sisi :"))
        print("Luas Persegi :", luas_persegi(s))
        
    elif pilih == 2:
        print("Menghitung Luas Persegi Panjang")
        p = int(input("Masukkan panjang :"))
        l = int(input("Masukkan lebar :"))
        print("Luas Persegi Panjang :", luas_persegi_panjang(p,l))
        
    elif pilih == 3:
        print("Menghitung Luas Segitiga")
        a = int(input("Masukkan alas :"))
        t = int(input("Masukkan tinggi :"))
        print("Luas Segitiga :", luas_segitiga(a,t))
        
    elif pilih == 4:
        print("Menghitung Luas Lingkaran")
        r = int(input("Masukkan jari-jari :"))
        print("Luas Lingkaran :", luas_lingkaran(r))
        
    elif pilih == 5:
        print("Menghitung Kelilins Persegi")
        s = int(input("Masukkan sisi :"))
        print("Kelilins Persegi :", keliling_persegi(s))
        
    elif pilih == 6:
        print("Menghitung Keliling Persegi Panjang")
        p = int(input("Masukkan panjang :"))
        l = int(input("Masukkan lebar :"))
        print("Keliling Persegi Panjang :", keliling_persegi_panjang(p,l))
        
    elif pilih == 7:
        print("Menghitung Keliling Segitiga")
        a = int(input("Masukkan panjang sisi A :"))
        b = int(input("Masukkan panjang sisi B :"))
        c = int(input("Masukkan panjang sisi C :"))
        print("Keliling Segitiga :", keliling_segitiga(a,b,c))
        
    elif pilih == 8:
        print("Menghitung Keliling Lingkaran")
        r = int(input("Masukkan jari-jari"))
        print("Keliling Lingkaran :", keliling_lingkaran(r))
        
    elif pilih == 9:
        print("Terima kasih telah menggunakan tools ini")
        print("Exit...")
        break
        
    else:
        print("Pilihan Anda Salah")
        
    ulang =""
    
    while ulang != "y" and ulang!= "t" :
        cls()
        ulang = input("Kembali ke menu utama [y/t] ? ")
        
    if ulang == "t":
        cls()
        print("Aplikasi Berhenti. Exit...")
        break
        
