from math import sqrt
from line import find_x_intercept

def make_quadratic(a, b, c):
    """Return a unary function which is callable with x, to return
    a floating point number equal to ax^2 + bx + c."""

    def f(x):
        return a * x**2 + b * x + c

    return f


def find_quadratic_coefficients(r1, r2):
    """Given two roots of a quadratic equation, find the coefficients, a, b, and c
    such that the roots of ax^2 + bx + c are r1 and r2.
    I.e., if f(x) = ax^2 + bx + c,
    then f(r1) = f(r2) = 0"""
    return sorted([1, 
                   -(r1 + r2), 
                   r1 * r2])

def find_quadratic_roots(a, b, c):
    """Given the coefficients of a quadratic equation, a, b, and c,
    of the equation ax^2 + bx + c, find all real roots and return them.
    In the case the quadratic equation has no real roots,
    return the empy list, [].
    In the case the quadratic equation has a single double root,
    return a list of that value twice. [r, r].
    Otherwise, return a list of the two real roots in increasing order,
    i.e., return [r1, r2] where r1 < r2.
    In the case that a == 0, the equation describes a line,
    return a list of its x-intercept.
    In the case that a and b are both zero, return the empty list, []"""
    epsilon = 0.001
    discriminant = b * b - 4 * a * c
    if a == 0 :
        return find_x_intercept(b,c)
    if discriminant > epsilon:
        return sorted([(-b + sqrt(discriminant)) / (2 * a),
                       (-b - sqrt(discriminant)) / (2 * a)])
    elif abs(discriminant) < epsilon:
        return [-b / (2 * a), 
                -b / (2 * a)]
    else:
        return []
