# Muhammad Bahrul Ulum - 2003691 - KOM-5A

import numpy as np
from math import sqrt


def my_newton(f, df, x0, e):

    print("Nilai xn: ", x0)

    if abs(f(x0)) < e:  
        return x0
    else:
        xn = x0 - f(x0)/df(x0)
        return my_newton(f, df, xn, e)


fx = lambda x: ((x**2)-(2*x)-8)

f_prime = lambda x: 2*x - 2

n = float(input())

estimate = my_newton(fx, f_prime, n, 1e-3)

print("estimate =", estimate)

