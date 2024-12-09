from cubic import find_cubic_coefficients

assert find_cubic_coefficients(1, 1, 1) == [1, -3, 3, -1]
assert find_cubic_coefficients(1, 2, 3) == [1, -6, 11, -6]
assert find_cubic_coefficients(1, 2, 3) == [1, -6, 11, -6]
assert find_cubic_coefficients(2, 1, 3) == [1, -6, 11, -6]
assert find_cubic_coefficients(3, 2, 1) == [1, -6, 11, -6]