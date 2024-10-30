from main import *

assert find_cubic_coefficients(1, 1, 1) == [1, -3, 3, -1]
assert find_cubic_coefficients(1, 2, 3) == [1, -6, 11, -6]
assert find_cubic_coefficients(1, 2, 3) == [1, -6, 11, -6]
assert find_cubic_coefficients(2, 1, 3) == [1, -6, 11, -6]
assert find_cubic_coefficients(3, 2, 1) == [1, -6, 11, -6]



#print(quartic_coefficients_from_roots(1,2,3,4))
print("============================")
r1, r2, r3, r4 = find_quartic_roots(1, -10, 35, -50, 24)
f = make_quartic(1, -10, 35, -50, 24)
print([r1, r2, r3, r4])
print([f(r1), f(r2), f(r3), f(r4)])

for r1 in range(-5, 5):
    for r2 in range(r1, 5):
        a, b, c = find_quadratic_coefficients(float(r1), float(r2))
        print([r1, r2, a, b, c])
        roots = find_quadratic_roots(a, b, c)
        for r3 in range(r2, 5):
            a, b, c, d = find_cubic_coefficients(float(r1), float(r2), float(r3))
            print([r1, r2, r3, a, b, c, d])
            roots = find_cubic_roots(a, b, c, d)
            for r4 in range(r3, 5):
                a, b, c, d, e = find_quartic_coefficients(float(r1), float(r2), float(r3), float(r4))
                print([r1, r2, r3, r4, a, b, c, d, e])
                roots = find_quartic_roots(a,b,c,d,e)


