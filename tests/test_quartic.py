import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "tests")))

from common import ImmTestCase, canonicalize

import_exception = None
try:
    from src.quartic import find_quartic_coefficients, find_quartic_roots
except Exception as e:
    print(e)
    import_exception = e


class QuarticTestCase(ImmTestCase):
    def test_code_check(self):
        self.code_check(["quartic.py"], import_exception)

    def test_quartic(self):
        epsilon = 0.001
        for r1 in range(-5, 5):
            for r2 in range(r1, 5):
                for r3 in range(r2, 5):
                    for r4 in range(r3, 5):
                        a, b, c, d, e = find_quartic_coefficients(float(r1), float(r2), float(r3), float(r4))
                        print([r1, r2, r3, r4, a, b, c, d, e])
                        roots = find_quartic_roots(a, b, c, d, e)
                        self.assertListAlmostEqual(canonicalize(roots, epsilon),
                                                   canonicalize([r1, r2, r3, r4], epsilon),
                                                   3)


if __name__ == '__main__':
    import unittest

    unittest.main()
