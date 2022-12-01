# Definisi fungsi
# def f(x):
#     return x**3-5*x-9

f = lambda x: x**2-6*x+8

# implementasi metode bagi dua
def bisection(a,b,e):  
   
    condition = True
    while condition:
        c = (a + b)/2  # c = (a+b)/2 --> new root formula

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        print(f(c))
        condition = abs(f(c)) > e


    print('\nRequired Root is : %0.8f' % c)


# Input Section
a = float(input('Masukan Nilai a: '))
b = float(input('Masukan Nilai b: '))
e = float(input('Masukan Nilai Galat: '))

# cek apakah terdapat akar?
if f(a) * f(b) > 0.0:
    print('Tidak Terdapat akar pada range ini!!!')
else:
    bisection(a,b,e)