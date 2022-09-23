# Muhammad Bahrul Ulum - 2003691 - KOM-5A

    import numpy as np
    from math import sqrt

#Inisiaslisasi fungsi dalam python 

    def newton_raps(f, df, x0, e):

        print("Nilai xn: ", x0)

        if abs(f(x0)) < e:  
            return x0
        else:
            xn = x0 - f(x0)/df(x0)
            return newton_raps(f, df, xn, e)

#Inisialisasi fungsi f(x) dan f'(x)
    
    fx = lambda x: ((x**2)-(2*x)-8)

    f_prime = lambda x: 2*x - 2 
    
#Inisialisasi nilai masukan dari x0 dan Pemanggilan fungsi "newton_raps"

    n = float(input())

    estimate = newton_raps(fx, f_prime, n, 1e-3)

    print("estimate =", estimate)
    
 #Akar dari fungsi f(x) = x^2 - 2x - 8 menggunakan metode Newton Raphson adalah 4,000..

