# Muhammad Tino Maulana
# NIM 2006129/5A
# Metode Newton Raphson

#Mendefinisikan fungsi Newton Raphson f(xn), f'(xn), xn, dan galat
def newton_raphson(f, df, x0, e):
    #Print nilai xn
    print("Nilai xn: ", x0)
    #Mengecek nilai mutlak
    if abs(f(x0)) < e:  
        #Jika benar, kembalikan nilai xn
        return x0
    #Jika salah, lanjutkan ke
    else:
        #Hitung xn+1
        xn = x0 - f(x0)/df(x0)
        #Memanggil kembali fungsi newton raphson
        return newton_raphson(f, df, xn, e)

#Mendefinisikan f(x)
fx = lambda x: ((x**2)-(2*x)-8)

#Mendefinisikan f'(x)
f_prime = lambda x: 2*x - 2

#Menentukan nilai x0
n = float(input())

#Memanggil fungsi newton rapson, 1e-3 => 10**-3 => 0,001
estimate = newton_raphson(fx, f_prime, n, 1e-3)

#Print estimasi x0 = 4,000...
print("estimate =", estimate)