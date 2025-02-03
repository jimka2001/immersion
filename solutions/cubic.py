from solutions.quadratic import find_quadratic_roots
from solutions.search import search_root_left, search_root_right
from solutions.polynomial import make_polynomial

epsilon = 0.0000001

def find_cubic_roots(a, b, c, d):
    """Given the coefficients of a cubic polynomial,
    compute the roots if possible.
    semantics of the coefficients are: P(x) = ax^3 + bx^2 + cx + d.
    If a == 0 (if absolute value of a < epsilon), re-used the function
    for computing the roots of a quadratic which you've already written.
    Do not repeat the code here, just call the existing code to get the
    quadratic roots and return them as a list.

    """

    if abs(a) < epsilon:
        # CHALLENGE: student must complete the implementation.
        return find_quadratic_roots(b, c, d)
    if a < 0:
        # Here we know the leading coefficients is negative,
        #   so we want to return the roots of -P(x) = -ax^3 - bx^2 - cx -d
        # CHALLENGE: student must complete the implementation.
        return find_cubic_roots(-a, -b, -c, -d)

    # compute a function, P, which can be called with a value of x, e.g., P(x).
    # P(x) returns the value of the cubic polynomial at x.
    P = make_polynomial([a,b,c,d])

    def find_one_root():
        if abs(d) < epsilon:
            # here we know the polynomial is 0 at x=0, P(0)=0, so it has
            # a root at 0, so return 0.0
            # CHALLENGE: student must complete the implementation.
            return 0.0
        elif d > 0:
            # P(0) = d, so P(-infinity) < 0 and P(infinity) > 0.
            # Here we know the polynomial is strictly positive at x=0,
            # so the polynomial becomes negative somewhere to the left.
            # Thus, we perform a search in the leftward direction to find a root.
            return search_root_left(-1, 0, P, epsilon)
        else:
            # P(0) = d, so P(-infinity) < 0 and P(infinity) > 0
            # Here we know the polynomial is strictly negative at x=0,
            # so the polynomial becomes positive somewhere to the right.
            # Thus, we perform a search in the rightward direction to find a root.
            # CHALLENGE: student must complete the implementation.
            return search_root_right(0, 1, P, epsilon)

    r = find_one_root()

    A = (
        # When we factor ax^3 + bx^2 + cx + d = (x-r)(Ax^2 + Bx + C)
        # what is the formula for A?
        # The formulas for A, B, and are found in the file polynomials.pdf
        #   in Section 7: Cubic: degree=3.
        # CHALLENGE: student must complete the implementation.
        a
    )
    B = (
        # When we factor ax^3 + bx^2 + cx + d = (x-r)(Ax^2 + Bx + C)
        # what is the formula for B?
        # The formulas for A, B, and are found in the file polynomials.pdf
        #   in Section 7: Cubic: degree=3.
        # CHALLENGE: student must complete the implementation.
        b + A * r
    )
    C = (
        # When we factor ax^3 + bx^2 + cx + d = (x-r)(Ax^2 + Bx + C)
        # what is the formula for C?
        # The formulas for A, B, and are found in the file polynomials.pdf
        #   in Section 7: Cubic: degree=3.
        # CHALLENGE: student must complete the implementation.
        c + B * r
    )

    # Now we have found a root, r.  We simply prepend [r]
    #  to the list of roots of the polynomial which remains
    #  after dividing P(x) / (x-r),
    return [r] + find_quadratic_roots(A, B, C)
