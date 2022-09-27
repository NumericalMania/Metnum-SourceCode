# Chintya Olivianita Pormes
# NIM 2007637
# KOM 5A

#Inisialisai fungsi untuk menghitung f(xn), f'(xn), xn, dan e menggunakan metode Newton Raphson
def newton_raphson(f, df, x0, e):
    #Cetak nilai xn
    print("Nilai xn: ", x0)
    #Jika |f(xn)<e|
    if abs(f(x0)) < e:  
        #Kembalikan nilai xn
        return x0
    else:
        #Perhitungan xn+1 (xn selanjutnya)
        xn = x0 - f(x0)/df(x0)
        #Kembalikan nilai f(xn), f'(xn), xn, dan e yang baru setelah melalui perhitungan
        return newton_raphson(f, df, xn, e)

#Definisikan f(x)
#Lambda disini merupakan ekspresi untuk membuat fungsi
#Dengan lambda, kita tidak perlu menggunakan def dan return (lebih ringkas)
fx = lambda x: ((x**2)-(2*x)-8)

#Definisikan f'(x)
f_prime = lambda x: 2*x - 2

#Masukkan nilai awal (x0)
n = float(input())

#Pemanggilan fungsi newton_raps
#1e-3 artinya 10**-3 (10 pangkat -3) -> 0,001
estimate = newton_raphson(fx, f_prime, n, 1e-3)

#Cetak akar persamaan yang dihasilkan (nilai xn terakhir yang diperoleh dari perhitungan fungsi newton_raps)
#xn terakhir -> 4,000...
print("estimate =", estimate)
