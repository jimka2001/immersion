from src.cubic import find_cubic_roots
from src.search import find_root_in_range, search_root_left, search_root_right


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

def find_quartic_roots(a, b, c, d, e):
    """If P(x) is a quartic polynomial of the form
    P(x) = ax^4 + bx^3 + cx^2 + dx + e,
    then it has up to 4 roots.  I.e., there are at most 4 real numbers, x
    for which p(x) = 0.
    The goal of this function, find_quartic_roots, is to return a sorted list
    of as many of those roots as possible.
    """
    epsilon = 0.00001
    if a == 0:
        # Since a=0, then the polynomial can be solved by the previous solution in cubic.py.
        # The student should insert a return and function call to the previously defined
        # function with the correct coefficients of the cubic polynomial.
        # CHALLENGE: student must complete the implementation.
        return find_cubic_roots(b, c, d, e)
    if a < 0:
        # Since the leading coefficient of P(x) = ax^4 + bx^3 + cx^2 + dx + e,
        # is negative, we instead want to compute the roots of -P(x) = -ax^4 - bx^3 - cx^2 - dx - e.
        # We need to make a recursive call with the arguments negated.
        # CHALLENGE: student must complete the implementation.
        return find_quartic_roots(-a, -b, -c, -d, -e)


    def find_one_root():
        ips = sorted(
            # The derivative of a degree 4 polynomial is a degree 3 polynomial.
            # The roots of the degree 3 tells us the inflection points of the
            # degree 4 polynomial.
            # Here the goal is to compute the roots of the degree 3 (cubic)
            # polynomial using functions developed earlier in cubic.py
            # Recall the derivative of ax^4 + bx^3 + cx^2 + dx +e
            #  = 4ax^3 + 3bx^2 + 2cx + d
            #
            # CHALLENGE: student must complete the implementation.
            find_cubic_roots(4 * a, 3 * b, 2 * c, d)
        )
        P = make_quartic(a, b, c, d, e)

        for ip in ips:
            # if the polynomial is 0 at one of the inflection points,
            # then the inflection point is the root
            if abs(P(ip)) < epsilon:
                return ip
    
        if P(ips[0]) < 0 < P(ips[1]):
            # Find a root between ips[0] and ips[1]
            # CHALLENGE: student must complete the implementation.
            return find_root_in_range(ips[0], ips[1], P, epsilon)
        if P(ips[1]) < 0 < P(ips[2]):
            # Find a root between ips[1] and ips[0]
            # CHALLENGE: student must complete the implementation.
            return find_root_in_range(ips[1], ips[2], P, epsilon)
        if P(ips[0]) < 0:
            # Find a root to the left of ips[0]
            # CHALLENGE: student must complete the implementation.
            return search_root_left(ips[0] - 1, ips[0], P, epsilon)
        if P(ips[-1]) < 0:
            # ips[-1] is the right-most inflection point.
            # Find a root to the right of ips[-1]
            return search_root_right(ips[-1], ips[-1] + 1, P, epsilon)

    r = find_one_root()

    A = (
        # When we factor ax^4 + bx^3 + cx^2 + dx + e = (x-r)(Ax^3 + Bx^2 + Cx + D)
        # what is the formula for A?
        # CHALLENGE: student must complete the implementation.
        a
    )
    B = (
        # When we factor ax^4 + bx^3 + cx^2 + dx + e = (x-r)(Ax^3 + Bx^2 + Cx + D)
        # what is the formula for B?
        # CHALLENGE: student must complete the implementation.
        b + r * A
    )
    C = (
        # When we factor ax^4 + bx^3 + cx^2 + dx + e = (x-r)(Ax^3 + Bx^2 + Cx + D)
        # what is the formula for C?
        # CHALLENGE: student must complete the implementation.
        c + r * B
    )
    D = (
        # When we factor ax^4 + bx^3 + cx^2 + dx + e = (x-r)(Ax^3 + Bx^2 + Cx + D)
        # what is the formula for D?
        # CHALLENGE: student must complete the implementation.
        d + r * C
    )
    return [r] + find_cubic_roots(A, B, C, D)
