from math import sqrt


def compute_cubic_coefficients_from_roots(r1, r2, r3):
    """Return a tuple of 4 numbers which represent
    coefficients of a polynomial having r1, r2, and r3
    as roots.  if the tuple returned is (a,b,c,d),
    then the polynomial is ax^3 + bx^2 + cx + d"""
    return [1,
            -r1 + r2 + r3,
            r1 * r2 + r2 * r3 + r1 * r3,
            -r1 * r2 * r3]


def compute_quadratic_roots_from_coefficients(a, b, c):
    epsilon = 0.00001
    discriminant = b * b - 4 * a * c

    if abs(discriminant) < epsilon:
        return []
    elif discriminant > 0:
        return [(-b + sqrt(discriminant)) / (2 * a),
                (-b - sqrt(discriminant)) / (2 * a)]
    else:
        return [-b / (2 * a),
                -b / (2 * a)]


def find_root_in_range(lower, upper, f, epsilon):
    mid = (lower + upper) / 2.0
    if upper - lower < epsilon:
        return mid
    fl = f(lower)
    fm = f(mid)
    if fl * fm <= 0:  # different signs
        return find_root_in_range(lower, mid, f, epsilon)
    else:
        return find_root_in_range(mid, upper, f, epsilon)


def find_window(lower, upper, f):
    if f(lower) * f(upper) < 0:  # different signs at endpoint
        return [lower, upper]
    else:
        delta = upper - lower
        return find_window(lower - delta, upper + delta)


def compute_cubic_roots_from_coefficients(a, b, c, d):
    """Given the coefficients of a cubic polynomial,
    compute the roots if possible.
    semantics of the coefficients are: ax^3 + bx^2 + cx + d
    """
    if a < 0:
        return compute_cubic_roots_from_coefficients(-a, -b, -c, -d)

    def f(x):
        return a * x ** 3 + b * x ** 2 + c * x + d

    lower, upper = find_window(-1.0, 1.0, f)
    r1 = find_root_in_range(lower, upper, f)
    A = a
    B = b + A * r1
    C = c + B * r1
    r2r3 = compute_quadratic_roots_from_coefficients(A, B, C)
    if r2r3:
        r2, r3 = r2r3
        return [r1, r2, r3]
    else:
        return [r1]
