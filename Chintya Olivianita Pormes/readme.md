# Chintya Olivianita Pormes - 2007637 - KOM 5A

#Inisialisai fungsi untuk menghitung f(xn), f'(xn), xn, dan e menggunakan metode Newton Raphson

    def newton_raps(f, df, x0, e):

        print("Nilai xn: ", x0)

        if abs(f(x0)) < e:  
            return x0
        else:
            xn = x0 - f(x0)/df(x0)
            return newton_raps(f, df, xn, e)
        
#Definisikan f(x)

    fx = lambda x: ((x**2)-(2*x)-8)

#Definisikan f'(x)

    f_prime = lambda x: 2*x - 2

#Masukkan nilai awal (x0)

    n = float(input())

#Pemanggilan fungsi newton_raps

    estimate = newton_raphson(fx, f_prime, n, 1e-3)
    
#Cetak akar persamaan yang dihasilkan (nilai xn terakhir yang diperoleh dari perhitungan fungsi newton_raps)

    print("estimate =", estimate)
