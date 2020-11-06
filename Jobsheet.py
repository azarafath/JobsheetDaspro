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
