from math import sqrt

def make_cubic(a,b,c,d):
    def f(x):
        return a * x ** 3 + b * x ** 2 + c * x + d
    return f

def make_quartic(a,b,c,d,e):
    def f(x):
        return a * x ** 4 + b * x ** 3 + c * x**2 + d*x + e
    return f

def cubic_coefficients_from_roots(r1, r2, r3):
    """Return an array of 4 numbers which represent
    coefficients of a polynomial having r1, r2, and r3
    as roots.  if the array returned is [a,b,c,d],
    then the polynomial is ax^3 + bx^2 + cx + d"""
    return [1,
            -(r1 + r2 + r3),
            r1 * r2 + r2 * r3 + r1 * r3,
            -r1 * r2 * r3]

def quartic_coefficients_from_roots(r1, r2, r3, r4):
    return [1,
            -(r1 + r2 + r3 + r4),
            r1 * r2 + r1*r3 + r1*r4 + r2*r3 + r2*r4 + r3*r4,
            -(r1*r2*r3 + r1*r2*r4 + r1*r3*r4 + r2*r3*r4),
            r1*r2*r3*r4]


def quadratic_roots(a, b, c):
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
    # print(f"searching for root in range [{lower}, {upper}]")
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
        return find_window(lower - delta, upper + delta, f)


def cubic_roots(a, b, c, d):
    """Given the coefficients of a cubic polynomial,
    compute the roots if possible.
    semantics of the coefficients are: ax^3 + bx^2 + cx + d
    """
    if a == 0:
        return quadratic_roots(b,c,d)
    if a < 0:
        return cubic_roots(-a, -b, -c, -d)

    f = make_cubic(a,b,c,d)

    lower, upper = find_window(-1.0, 1.0, f)
    r1 = find_root_in_range(lower, upper, f, 0.00001)
    A = a
    B = b + A * r1
    C = c + B * r1
    r2r3 = quadratic_roots(A, B, C)
    if r2r3:
        r2, r3 = r2r3
        return [r1, r2, r3]
    else:
        return [r1]

# print(cubic_roots(1, -6, 11, -6))

def quartic_roots(a,b,c,d,e):
    epsilon = 0.00001
    if a == 0:
        return cubic_roots(b,c,d,e)
    if a < 0:
        return quartic_roots(-a, -b, -c, -d, -e)
    # derivative of ax^4 + bx^3 + cx^2 + dx +e
    #  = 4ax^3 + 3bx^2 + 2cx + d
    inflection_points = cubic_roots(4*a, 3*b, 2*c, d)
    inflection_points.sort()
    f = make_quartic(a,b,c,d,e)
    def factor_out_root(r):
        A = a
        B = b + r * A
        C = c + r * B
        D = d + r * C
        return cubic_roots(A, B, C, D) + [r]

    for i in [0,1]:
        if f(inflection_points[i]) < 0 < f(inflection_points[i+1]) :
            print("case 1")
            r = find_root_in_range(inflection_points[i], inflection_points[i+1], f, epsilon)
            return factor_out_root(r)
    if f(inflection_points[0]) < 0:
        print("case 2")
        upper = inflection_points[1]
        delta = 1
        while f(upper - delta) < 0:
            delta *= 2
        r = find_root_in_range(upper - delta, upper, f, epsilon)
        return factor_out_root(r)
    if f(inflection_points[-1]) < 0:
        print("case 3")
        lower = inflection_points[-1]
        delta = 1
        while f(lower + delta) < 0:
            delta *= 2
        r = find_root_in_range(lower, lower + delta, f, epsilon)
        return factor_out_root(r)


