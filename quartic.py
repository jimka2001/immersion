from cubic import find_cubic_roots
from search import find_root_in_range, search_root_left, search_root_right


def make_quartic(a, b, c, d, e):
    def f(x):
        return a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e

    return f


def find_quartic_coefficients(r1, r2, r3, r4):
    return [1,
            -(r1 + r2 + r3 + r4),
            r1 * r2 + r1 * r3 + r1 * r4 + r2 * r3 + r2 * r4 + r3 * r4,
            -(r1 * r2 * r3 + r1 * r2 * r4 + r1 * r3 * r4 + r2 * r3 * r4),
            r1 * r2 * r3 * r4]

def factor_out_quartic_root(r, a, b, c, d):
    A = a
    B = b + r * A
    C = c + r * B
    D = d + r * C
    return sorted(find_cubic_roots(A, B, C, D) + [r])


def find_quartic_roots(a, b, c, d, e):
    epsilon = 0.00001
    if a == 0:
        return find_cubic_roots(b, c, d, e)
    if a < 0:
        return find_quartic_roots(-a, -b, -c, -d, -e)
    # derivative of ax^4 + bx^3 + cx^2 + dx +e
    #  = 4ax^3 + 3bx^2 + 2cx + d
    inflection_points = sorted(find_cubic_roots(4 * a, 3 * b, 2 * c, d))
    f = make_quartic(a, b, c, d, e)

    for i in [0, 1]:
        if f(inflection_points[i]) < 0 < f(inflection_points[i + 1]):
            r = find_root_in_range(inflection_points[i], inflection_points[i + 1], f, epsilon)
            return factor_out_quartic_root(r, a, b, c, d)
    if f(inflection_points[0]) < 0:
        r = search_root_left(inflection_points[0] - 1, inflection_points[0], f, epsilon)
        return factor_out_quartic_root(r, a, b, c, d)
    if f(inflection_points[-1]) < 0:
        r = search_root_right(inflection_points[-1], inflection_points[-1] + 1, f, epsilon)
        return factor_out_quartic_root(r, a, b, c, d)
