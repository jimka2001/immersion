def compute_cubic_coefficients_from_roots(r1, r2, r3):
    """Return a tuple of 4 numbers which represent
    coefficients of a polynomial having r1, r2, and r3
    as roots.  if the tuple returned is (a,b,c,d),
    then the polynomial is ax^3 + bx^2 + cx + d"""
    return (1,
            -r1 + r2 + r3,
            r1 * r2 + r2 * r3 + r1 * r3,
            -r1 * r2 * r3)


def compute_roots_from_coefficients(a, b, c, d):
    """Given the coefficients of a cubic polynomial,
    compute the roots if possible.
    semantics of the coefficients are: ax^3 + bx^2 + cx + d
    """
    pass
