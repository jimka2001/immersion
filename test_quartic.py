from quartic import make_quartic, find_quartic_roots

r1, r2, r3, r4 = find_quartic_roots(1, -10, 35, -50, 24)
f = make_quartic(1, -10, 35, -50, 24)
print([r1, r2, r3, r4])
print([f(r1), f(r2), f(r3), f(r4)])
