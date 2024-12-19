from solutions.polynomial import make_polynomial_from_coefficients


def search_root_left(lower, upper, P, epsilon):
    """Search to the left of lower to find an x value for which P(x) is
    sufficiently close to 0."""
    assert upper > lower
    if P(upper) * P(lower) < 0:
        return find_root_in_range(lower, upper, P, epsilon)
    else:  # if same sign
        delta = upper - lower
        assert delta > 0
        return search_root_left(lower - delta, upper, P, epsilon)


def search_root_right(lower, upper, P, epsilon):
    """search to the right of upper to find an x value for which P(x) is
    sufficiently close to 0."""
    assert upper > lower

    if P(upper) * P(lower) < 0:  # if different sign
        # We know the polynomial has different signs at upper and lower,
        #  therefore it crosses the x-axis somewhere between lower and upper.
        #  Insert a call to the function, find_root_in_range, with the
        #  four correct arguments.  Use the code for search_root_left
        #  as an example.
        # CHALLENGE: student must complete the implementation.
        return find_root_in_range(lower, upper, P, epsilon)
    else:
        # We know the polynomial has the same sign at upper and lower,
        # but change some at some x to the right.
        # Insert a call to the function, search_root_right, with the
        # correct four arguments.  use the code for search_root_left
        # as an example.
        # CHALLENGE: student must complete the implementation.
        delta = upper - lower
        assert delta > 0
        return search_root_right(lower, upper + delta, P, epsilon)


def find_root_in_range(lower, upper, P, epsilon):
    """If we know there is a root of P between lower and upper,
    this function will return a number (value of x) very
    close to such a root.  This function will return an x value which is
    1.  between lower and upper:  lower <= x <= upper,
    2.  P(x) is small in absolute value:
           P(x+epsilon) >= 0 and P(x-epsilon)= < 0
        or
           P(x+epsilon) <= 0 and P(x-epsilon) >= 0
    """
    mid = (lower + upper) / 2.0
    if upper - lower < epsilon / 2.0:
        return mid
    fl = P(lower)
    fm = P(mid)
    if fl * fm <= 0:  # different signs
        return find_root_in_range(lower, mid, P, epsilon)
    else:
        return find_root_in_range(mid, upper, P, epsilon)
