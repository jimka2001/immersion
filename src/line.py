epsilon = 0.000001

def find_x_intercept(a,b):
    """Compute the x-intercept of the line whose equation is y=ax+b.
       The x-intercept is returned as a list of a number, or empty
       list if the (unique) x-intercept cannot be determined.
       If a=0, we conclude that there is no (unique) x-intercept so
       we return [], an empty list.
       Otherwise, the x-intercept is given by the formula -b/a.
       """
    if abs(a) < epsilon:
        # CHALLENGE: student must complete the implementation.
        # HINT: goal = 1 line of code
        return []

    else:
        # CHALLENGE: student must complete the implementation.
        # HINT: goal = 1 line of code
        return [-b/a]

