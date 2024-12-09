from cubic import find_cubic_coefficients, find_cubic_roots
from quadratic import find_quadratic_coefficients, find_quadratic_roots
from quartic import find_quartic_coefficients, find_quartic_roots

#print(quartic_coefficients_from_roots(1,2,3,4))
print("============================")

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


