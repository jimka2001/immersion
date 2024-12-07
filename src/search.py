def search_root_left(lower, upper, f, epsilon):
    """search to the left of lower to find an x value for which f(x) is
    sufficiently close to 0."""
    assert upper > lower
    if f(upper) * f(lower) < 0:
        return find_root_in_range(lower, upper, f, epsilon)
    else:  # if same sign
        delta = upper - lower
        assert delta > 0
        return search_root_left(lower - delta, upper, f, epsilon)


def search_root_right(lower, upper, f, epsilon):
    """search to the right of upper to find an x value for which f(x) is
    sufficiently close to 0."""
    assert upper > lower
    if f(upper) * f(lower) < 0:  # if different sign
        return find_root_in_range(lower, upper, f, epsilon)
    else:
        delta = upper - lower
        assert delta > 0
        return search_root_right(lower, upper + delta, f, epsilon)


def find_root_in_range(lower, upper, f, epsilon):
    """If we know there is a root of f between lower and upper,
    this function will return a number (value of x) very
    close to such a root.  This function will return an x value which is
    1.  between lower and upper:  lower <= x <= upper,
    2.  f(x) is small in absolute value:
           f(x+epsilon) >= 0 and f(x-epsilon)= < 0
        or
           f(x+epsilon) <= 0 and f(x-epsilon) >= 0
    """
    mid = (lower + upper) / 2.0
    if upper - lower < epsilon / 2.0:
        return mid
    fl = f(lower)
    fm = f(mid)
    if fl * fm <= 0:  # different signs
        return find_root_in_range(lower, mid, f, epsilon)
    else:
        return find_root_in_range(mid, upper, f, epsilon)
