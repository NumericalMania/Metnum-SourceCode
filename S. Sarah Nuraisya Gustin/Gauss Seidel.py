# Gauss Seidel 

f1 = lambda a, b, c, d, e: (5 + 2 * b + c) / 8
f2 = lambda a, b, c, d, e: (2 + 2 * a + 4 * c + d) / 9
f3 = lambda a, b, c, d, e: (a + 3 * b + d + 2 * e) / 7
f4 = lambda a, b, c, d, e: (1 + 4 * b + 2 * c + 5 * e) / 12
f5 = lambda a, b, c, d, e: (5 + 7 * c + 3 * d) / 15

a0 = 0
b0 = 0
c0 = 0
d0 = 0
e0 = 0

count = 1

# Galat 
eps = 0.0001

print('\nHitung\ta\tb\tc\td\te\n')

condition = True

while condition:
    a1 = f1(a0, b0, c0, d0, e0)
    b1 = f2(a1, b0, c0, d0, e0)
    c1 = f3(a1, b1, c0, d0, e0)
    d1 = f4(a1, b1, c1, d0, e0)
    e1 = f4(a1, b1, c1, d1, e0)

    print('%d\t%0.4f\t%0.4f\t%0.4f\t%0.4f\t%0.4f\n' % (count, a1, b1, c1, d1, e1))
    ep1 = abs(a0 - a1)
    ep2 = abs(b0 - b1)
    ep3 = abs(c0 - c1)
    ep4 = abs(d0 - d1)
    ep5 = abs(e0 - e1)

    count += 1
    a0 = a1
    b0 = b1
    c0 = c1
    d0 = d1
    e0 = e1

    condition = ep1 > eps and ep2 > eps and ep3 > eps and ep4 > eps and ep5 > eps

print('\nSolusi: a=%0.4f, b=%0.4f, c=%0.4f, d=%0.4f and eps = %0.4f\n' % (a1, b1, c1, d1, e1))