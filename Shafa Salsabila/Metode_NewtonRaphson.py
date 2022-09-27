#Shafa Salsabila
#2003467
#Metode Numerik KOM-5A

#step 5 : menjalankan fungsi newton raphson
def newton_raphson(f, df, x0, e):

    #step 6 : print nilai xn
    print("Nilai xn: ", x0)

    # step 7 : menghitung nilai mutlak
    # jika nilai mutlak lebih kecil dari 0,001 maka return x0 atau program berhenti
    if abs(f(x0)) < e:  
        return x0
    
    # jika nilai mutlak tidak lebih kecil dari 0,001, maka buat xn baru dengan rumus di bawah
    else:
        xn = x0 - f(x0)/df(x0)
        # panggil kembali fungsi newton raphson
        return newton_raphson(f, df, xn, e)

#step 1: lambda-> anonymous function untuk sebuah fungsi
fx = lambda x: ((x**2)-(2*x)-8)

#step 2 : mencari turunan dari fungsi
f_prime = lambda x: 2*x - 2

#step 3 : menentukan nilai tebakan untuk x0, misalnya 6
n = float(input())

#step 4: memanggil fungsi newton raphson dengan 4 parameter fx, f_prime, n, dan 1e-3
#1e-3: 10**3 -> 0,001
estimate = newton_raphson(fx, f_prime, n, 1e-3)

# estimate = x0 -> 4.0000...
print("estimate =", estimate)