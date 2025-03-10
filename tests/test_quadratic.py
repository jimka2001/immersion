import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "tests")))

from common import ImmTestCase, canonicalize
from src.polynomial import find_quadratic_coefficients

import_exception = None
try:
    from src.quadratic import find_quadratic_roots
except Exception as e:
    print(e)
    import_exception = e


class QuadraticTestCase(ImmTestCase):
    def test_code_check(self):
        self.code_check(["quadratic.py"], import_exception)

    def test_quadratic(self):
        epsilon = 0.0001
        for r1 in range(-5, 5):
            for r2 in range(r1, 5):
                a, b, c = find_quadratic_coefficients(float(r1), float(r2))
                print([r1, r2, a, b, c])
                roots = find_quadratic_roots(a, b, c)
                self.assertTrue(isinstance(roots, list), "return value of find_quadratic_roots should be a list")
                self.assertListAlmostEqual(canonicalize(roots, epsilon),
                                           canonicalize([r1, r2], epsilon),
                                           3)


if __name__ == '__main__':
    import unittest

    unittest.main()
