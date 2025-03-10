import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "tests")))

from common import ImmTestCase, canonicalize
from src.polynomial import find_cubic_coefficients

import_exception = None
try:
    from src.cubic import find_cubic_roots
except Exception as e:
    print(e)
    import_exception = e


class CubicTestCase(ImmTestCase):
    def test_code_check(self):
        self.code_check(["cubic.py"], import_exception)

    def test_static_cubic(self):
        self.assertEqual( find_cubic_coefficients(1, 1, 1),
                          [1, -3, 3, -1])
        self.assertEqual( find_cubic_coefficients(1, 2, 3),
                          [1, -6, 11, -6])
        self.assertEqual( find_cubic_coefficients(1, 2, 3),
                          [1, -6, 11, -6])
        self.assertEqual( find_cubic_coefficients(2, 1, 3),
                          [1, -6, 11, -6])
        self.assertEqual( find_cubic_coefficients(3, 2, 1),
                          [1, -6, 11, -6])

    def test_cubic(self):
        epsilon = 0.0001
        for r1 in range(-5, 5):
            for r2 in range(r1, 5):
                for r3 in range(r2, 5):
                    a, b, c, d = find_cubic_coefficients(float(r1), float(r2), float(r3))
                    roots = find_cubic_roots(a, b, c, d)
                    self.assertTrue(isinstance(roots, list),
                                    "return value of find_cubic_roots should be a list")
                    self.assertListAlmostEqual(canonicalize(roots, epsilon),
                                               canonicalize([r1, r2, r3], epsilon),
                                               3)


if __name__ == '__main__':
    import unittest

    unittest.main()
