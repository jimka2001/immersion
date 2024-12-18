from src.quadratic import find_quadratic_roots
from src.search import search_root_left, search_root_right
from src.polynomial import make_cubic



def find_cubic_roots(a, b, c, d):
    """Given the coefficients of a cubic polynomial,
    compute the roots if possible.
    semantics of the coefficients are: P(x) = ax^3 + bx^2 + cx + d
    """
    epsilon = 0.00001
    if a == 0:
        # CHALLENGE: student must complete the implementation.
        return find_quadratic_roots(b, c, d)
    if a < 0:
        # Here we know the leading coefficients is negative,
        #   so we want to return the roots of -P(x) = -ax^3 - bx^2 - cx -d
        # CHALLENGE: student must complete the implementation.
        return find_cubic_roots(-a, -b, -c, -d)

    P = make_cubic(a, b, c, d)
    def find_one_root():
        if d == 0.0:
            # here we know the polynomial is 0 at x=0, P(0)=0, so it has
            # a root at 0, so return 0.0
            # CHALLENGE: student must complete the implementation.
            return 0.0
        elif d > 0:
            # P(0) = d, so P(-infinity) < 0 and P(infinity) > 0
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
        # CHALLENGE: student must complete the implementation.
        a
    )
    B = (
        # When we factor ax^3 + bx^2 + cx + d = (x-r)(Ax^2 + Bx + C)
        # what is the formula for B?
        # CHALLENGE: student must complete the implementation.
        b + A * r
    )
    C = (
        # When we factor ax^3 + bx^2 + cx + d = (x-r)(Ax^2 + Bx + C)
        # what is the formula for C?
        # CHALLENGE: student must complete the implementation.
        c + B * r
    )

    return [r] + find_quadratic_roots(A, B, C)
