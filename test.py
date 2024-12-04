from main import *

assert find_cubic_coefficients(1, 1, 1) == [1, -3, 3, -1]
assert find_cubic_coefficients(1, 2, 3) == [1, -6, 11, -6]
assert find_cubic_coefficients(1, 2, 3) == [1, -6, 11, -6]
assert find_cubic_coefficients(2, 1, 3) == [1, -6, 11, -6]
assert find_cubic_coefficients(3, 2, 1) == [1, -6, 11, -6]



r1, r2, r3, r4 = find_quartic_roots(1, -10, 35, -50, 24)
f = make_quartic(1, -10, 35, -50, 24)

bound = 25
for r1 in range(-bound, bound):
    print(f"{r1=}")
    for r2 in range(r1, bound):
        a, b, c = find_quadratic_coefficients(float(r1), float(r2))
        roots = find_quadratic_roots(a, b, c)
        assert roots
        roots.sort()
        assert len(roots) == 2
        epsilon = 0.01
        assert abs(roots[0] - r1) < epsilon, f"{roots=}, {r1=}"
        assert abs(roots[1] - r2) < epsilon, f"{roots=}, {r2=}"
        for r3 in range(r2, bound):
            a, b, c, d = find_cubic_coefficients(float(r1), float(r2), float(r3))
            roots = find_cubic_roots(a, b, c, d)
            assert roots
            roots.sort()
            assert len(roots) == 3
            epsilon = 0.01
            assert abs(roots[0] - r1) < epsilon, f"{roots=}, {r1=}"
            assert abs(roots[1] - r2) < epsilon, f"{roots=}, {r2=}"
            assert abs(roots[2] - r3) < epsilon, f"{roots=}, {r3=}"
            for r4 in range(r3, bound):
                a, b, c, d, e = find_quartic_coefficients(float(r1), float(r2), float(r3), float(r4))
                roots = find_quartic_roots(a, b, c, d, e)

                assert roots and len(roots) == 4, f"{roots=} failed to find 4 roots of {r1=} {r2=} {r3=} {r4=} {a=} {b=} {c=} {d=} {e=}"
                roots.sort()
                epsilon = 0.01
                assert abs(roots[0] - r1) < epsilon, f"{roots=}, {r1=}"
                assert abs(roots[1] - r2) < epsilon, f"{roots=}, {r2=}"
                assert abs(roots[2] - r3) < epsilon, f"{roots=}, {r3=}"
                assert abs(roots[3] - r4) < epsilon, f"{roots=}, {r4=}"
