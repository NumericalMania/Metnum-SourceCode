import numpy as np #panggil library

def my_newton(f, df, x0, e):

    print("Nilai xn: ", x0)
#absmutlak
    if abs(f(x0)) < e:  
        return x0
    else:
        xn = x0 - f(x0)/df(x0)
        return my_newton(f, df, xn, e)

#lamda ekspresi untuk membuat fungsi 
#fx0
fx = lambda x: ((x**2)-(2*x)-8)

#fx aksen 0
f_prime = lambda x: 2*x - 2

#nilai tebakan awal x0
n = float(input())

#1e-3: 10**3 -> 0.001
estimate = my_newton(fx, f_prime, n, 1e-3)

#estimate = x0
print("estimate =", estimate)