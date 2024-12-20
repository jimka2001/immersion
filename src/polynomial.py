def make_polynomial(coefs):
    """Given the 5 coefficients of a degree 4 polynomial, return a unary
    function which will evaluate the polynomial at a given x value."""
    assert isinstance(coefs, list)
    degree = len(coefs) - 1

    def f(x):
        return sum(c * (x ** (degree - p)) for (p, c) in enumerate(coefs))

    return f


def find_quadratic_coefficients(r1, r2):
    """Given two roots of a quadratic equation, find the coefficients, a, b, and c
    such that the roots of ax^2 + bx + c are r1 and r2.
    I.e., if f(x) = ax^2 + bx + c,
    then f(r1) = f(r2) = 0"""
    return [1,
            -(r1 + r2),
            r1 * r2]


def find_cubic_coefficients(r1, r2, r3):
    """Return an array of 4 numbers which represent
    coefficients of a polynomial having r1, r2, and r3
    as roots.  if the array returned is [a,b,c,d],
    then the polynomial is ax^3 + bx^2 + cx + d"""
    return [1,
            -(r1 + r2 + r3),
            r1 * r2 + r2 * r3 + r1 * r3,
            -r1 * r2 * r3]


def find_quartic_coefficients(r1, r2, r3, r4):
    """Given 4 roots of a degree 4 polynomial (quartic) return a list
    of 5 coefficients of a degree 4 polynomial which as those roots.
    """
    return [1,
            -(r1 + r2 + r3 + r4),
            r1 * r2 + r1 * r3 + r1 * r4 + r2 * r3 + r2 * r4 + r3 * r4,
            -(r1 * r2 * r3 + r1 * r2 * r4 + r1 * r3 * r4 + r2 * r3 * r4),
            r1 * r2 * r3 * r4]
