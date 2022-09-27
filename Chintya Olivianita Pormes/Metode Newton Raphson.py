# Chintya Olivianita Pormes
# NIM 2007637
# KOM 5A

def newton_raphson(f, df, x0, e):

    print("Nilai xn: ", x0)

    if abs(f(x0)) < e:  
        return x0
    else:
        xn = x0 - f(x0)/df(x0)
        return newton_raphson(f, df, xn, e)

#lambda: anonymous function 
fx = lambda x: ((x**2)-(2*x)-8)

f_prime = lambda x: 2*x - 2

n = float(input())

#1e-3: 10**3 -> 0,001
estimate = newton_raphson(fx, f_prime, n, 1e-3)

# estimate = x0 -> 4.0000sekian
print("estimate =", estimate)