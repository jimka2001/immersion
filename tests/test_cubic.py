import sys
import os
from tests.common import ImmTestCase

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "src")))

import_exception = None
try:
    from src.cubic import find_cubic_coefficients, find_cubic_roots
except Exception as e:
    print(e)
    import_exception = e

class CubicTestCase(ImmTestCase):
    def test_code_check(self):
        self.code_check([], import_exception)

    def test_cubic(self):
        assert find_cubic_coefficients(1, 1, 1) == [1, -3, 3, -1]
        assert find_cubic_coefficients(1, 2, 3) == [1, -6, 11, -6]
        assert find_cubic_coefficients(1, 2, 3) == [1, -6, 11, -6]
        assert find_cubic_coefficients(2, 1, 3) == [1, -6, 11, -6]
        assert find_cubic_coefficients(3, 2, 1) == [1, -6, 11, -6]
