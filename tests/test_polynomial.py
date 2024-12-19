import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "tests")))

from common import ImmTestCase, canonicalize

import_exception = None
try:
    from src.polynomial import make_polynomial
except Exception as e:
    print(e)
    import_exception = e


class PolynomialTestCase(ImmTestCase):
    def test_code_check(self):
        self.code_check(["polynomial.py"], import_exception)

    def test_static_polynomial(self):
        for x in range(-10, 10):
            for a in range(-5, 5):
                for b in range(a, 5):
                    for c in range(b, 5):
                        P = make_polynomial([a, b, c])
                        self.assertEqual(a*x**2 + b*x + c, P(x))


if __name__ == '__main__':
    import unittest

    unittest.main()
