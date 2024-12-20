from src.quadratic import find_quadratic_roots
from src.search import search_root_left, search_root_right
from src.polynomial import make_polynomial

epsilon = 0.0000001

def find_cubic_roots(a, b, c, d):
    """Given the coefficients of a cubic polynomial,
    compute the roots if possible.
    semantics of the coefficients are: P(x) = ax^3 + bx^2 + cx + d
    """

    if abs(a) < epsilon:
        # CHALLENGE: student must complete the implementation.
        # HINT: goal = 1 line of code
        raise NotImplementedError()

    if a < 0:
        # Here we know the leading coefficients is negative,
        #   so we want to return the roots of -P(x) = -ax^3 - bx^2 - cx -d
        # CHALLENGE: student must complete the implementation.
        # HINT: goal = 1 line of code
        raise NotImplementedError()

    P = make_polynomial([a,b,c,d])

    def find_one_root():
        if abs(d) < epsilon:
            # here we know the polynomial is 0 at x=0, P(0)=0, so it has
            # a root at 0, so return 0.0
            # CHALLENGE: student must complete the implementation.
            # HINT: goal = 1 line of code
            raise NotImplementedError()

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
            # HINT: goal = 1 line of code
            raise NotImplementedError()

    r = find_one_root()

    A = (
        # When we factor ax^3 + bx^2 + cx + d = (x-r)(Ax^2 + Bx + C)
        # what is the formula for A?
        # CHALLENGE: student must complete the implementation.
        # HINT: goal = 1 line of code
        raise NotImplementedError()

    )
    B = (
        # When we factor ax^3 + bx^2 + cx + d = (x-r)(Ax^2 + Bx + C)
        # what is the formula for B?
        # CHALLENGE: student must complete the implementation.
        # HINT: goal = 1 line of code
        raise NotImplementedError()

    )
    C = (
        # When we factor ax^3 + bx^2 + cx + d = (x-r)(Ax^2 + Bx + C)
        # what is the formula for C?
        # CHALLENGE: student must complete the implementation.
        # HINT: goal = 1 line of code
        raise NotImplementedError()

    )

    return [r] + find_quadratic_roots(A, B, C)
