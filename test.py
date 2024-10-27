from main import *

assert find_cubic_coefficients(1, 1, 1) == [1, -3, 3, -1]
assert find_cubic_coefficients(1, 2, 3) == [1, -6, 11, -6]
assert find_cubic_coefficients(1, 2, 3) == [1, -6, 11, -6]
assert find_cubic_coefficients(2, 1, 3) == [1, -6, 11, -6]
assert find_cubic_coefficients(3, 2, 1) == [1, -6, 11, -6]



#print(quartic_coefficients_from_roots(1,2,3,4))
print("============================")
r1, r2, r3, r4 = find_quartic_roots(1, -10, 35, -50, 24)
f = make_quartic(1, -10, 35, -50, 24)
print([r1, r2, r3, r4])
print([f(r1), f(r2), f(r3), f(r4)])