from src.quadratic import find_quadratic_roots
from src.search import search_root_left, search_root_right


def make_cubic(a, b, c, d):
    def f(x):
        return a * x ** 3 + b * x ** 2 + c * x + d

    return f


def find_cubic_coefficients(r1, r2, r3):
    """Return an array of 4 numbers which represent
    coefficients of a polynomial having r1, r2, and r3
    as roots.  if the array returned is [a,b,c,d],
    then the polynomial is ax^3 + bx^2 + cx + d"""
    return [1,
            -(r1 + r2 + r3),
            r1 * r2 + r2 * r3 + r1 * r3,
            -r1 * r2 * r3]


def factor_out_cubic_root(r, a, b, c):
    """Given a, b, c, and a root of a cubic polynomial, ax^3 + bx^2 + cx + d,
    It is possible to factor the polynomial into (x - r)(Ax^2 + Bx + C)
    (i.e., a different A, B, C probably not the same as a, b, c.)
    Then, we can use find_quadratic_roots to find the roots of the
    quadratic.
    This function, factor_out_cubic_root, returns a sorted list of the
    roots obtained by the algorithm described above."""
    A = a
    B = b + A * r
    C = c + B * r
    roots = find_quadratic_roots(A, B, C)
    return sorted([r] + roots)


def find_cubic_roots(a, b, c, d):
    """Given the coefficients of a cubic polynomial,
    compute the roots if possible.
    semantics of the coefficients are: ax^3 + bx^2 + cx + d
    """
    epsilon = 0.00001
    if a == 0:
        return find_quadratic_roots(b, c, d)
    if a < 0:
        return find_cubic_roots(-a, -b, -c, -d)

    f = make_cubic(a, b, c, d)

    if f(0.0) == 0.0:
        r = 0.0
    elif d > 0: # f(0) = d, so f(-infinity) < 0 and f(infinity) > 0
        r = search_root_left(-1, 0, f, epsilon)
    else:
        r = search_root_right(0, 1, f, epsilon)
    return factor_out_cubic_root(r, a, b, c)



