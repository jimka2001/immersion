
def make_quadratic(a, b, c):
    """Return a unary function which is callable with x, to return
    a floating point number equal to ax^2 + bx + c."""

    def f(x):
        return a * x ** 2 + b * x + c

    return f


def find_quadratic_coefficients(r1, r2):
    """Given two roots of a quadratic equation, find the coefficients, a, b, and c
    such that the roots of ax^2 + bx + c are r1 and r2.
    I.e., if f(x) = ax^2 + bx + c,
    then f(r1) = f(r2) = 0"""
    return [1,
            -(r1 + r2),
            r1 * r2]

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



def make_quartic(a, b, c, d, e):
    """Given the 5 coefficients of a degree 4 polynomial, return a unary
    function which will evaluate the polynomial at a given x value."""
    def f(x):
        return a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e

    return f


def find_quartic_coefficients(r1, r2, r3, r4):
    """Given 4 roots of a degree 4 polynomial (quartic) return a list
    of 5 coefficients of a degree 4 polynomial which as those roots.
    """
    return [1,
            -(r1 + r2 + r3 + r4),
            r1 * r2 + r1 * r3 + r1 * r4 + r2 * r3 + r2 * r4 + r3 * r4,
            -(r1 * r2 * r3 + r1 * r2 * r4 + r1 * r3 * r4 + r2 * r3 * r4),
            r1 * r2 * r3 * r4]