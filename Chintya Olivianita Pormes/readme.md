# Chintya Olivianita Pormes - 2007637 - KOM 5A

    # Fungsi untuk operasi perhitungan menggunakan metode Newton Raphson
        def newton_raphson(f, df, x0, e):

            print("Nilai xn: ", x0)

            if abs(f(x0)) < e:  
                return x0
            else:
                xn = x0 - f(x0)/df(x0)
                return newton_raphson(f, df, xn, e)

# Definisikan f(x)
    fx = lambda x: ((x**2)-(2*x)-8)

# Definisikan f'(x)
    f_prime = lambda x: 2*x - 2

# Tentukan nilai awal
    n = float(input())

# Pemanggilan fungsi newton_raphson
    estimate = newton_raphson(fx, f_prime, n, 1e-3)
    
# Cetak akar persamaan yang dihasilkan
    print("estimate =", estimate)
