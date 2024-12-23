from math import sqrt
from solutions.line import find_x_intercept

epsilon = 0.00001

def find_quadratic_roots(a, b, c):
    """Given the coefficients of a quadratic equation, a, b, and c,
    of the equation ax^2 + bx + c, find all real roots and return them.
    In the case the quadratic equation has no real roots,
    return the empy list, [].
    In the case the quadratic equation has a single double root,
    return a list of that value: [r].
    Otherwise, return a list of the two real roots in increasing order,
    i.e., return [r1, r2] where r1 < r2.
    In the case that a == 0, the equation describes a line,
    return a list of its x-intercept.
    In the case that a and b are both zero, return the empty list, []"""

    discriminant = b * b - 4 * a * c
    if abs(a) < epsilon:
        # invoke the previous solution for x-intercept of a line
        # CHALLENGE: student must complete the implementation.
        return find_x_intercept(b, c)
    if abs(discriminant) < epsilon:
        # Here we know the discriminant is very close to zero,
        #   so return a singleton list containing the one root.
        # CHALLENGE: student must complete the implementation.
        return [-b / (2 * a)]
    elif discriminant > 0:
        # Here we know the discriminant is not close to zero,
        #   and we also know it is positive, so we return a
        #   list containing the two roots according to the
        #   quadratic formula.
        # CHALLENGE: student must complete the implementation.
        return [(-b + sqrt(discriminant)) / (2 * a),
                (-b - sqrt(discriminant)) / (2 * a)]        
    else:
        # Here we know the discriminant is negative, so return an
        #    empty list of no roots.
        # CHALLENGE: student must complete the implementation.
        return []
