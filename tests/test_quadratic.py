import sys
import os
from tests.common import ImmTestCase

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "src")))

import_exception = None
try:
    from src.quadratic import find_quadratic_coefficients, find_quadratic_roots
except Exception as e:
    print(e)
    import_exception = e

class QuadraticTestCase(ImmTestCase):
    def test_code_check(self):
        self.code_check(["quadratic.py"], import_exception)

    def test_quadratic(self):
        for r1 in range(-5, 5):
            for r2 in range(r1, 5):
                a, b, c = find_quadratic_coefficients(float(r1), float(r2))
                print([r1, r2, a, b, c])
                roots = find_quadratic_roots(a, b, c)
                self.assertEqual(sorted(roots), sorted([r1, r2]))


