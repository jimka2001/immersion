import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "tests")))

from common import ImmTestCase

import_exception = None
try:
    from src.line import find_x_intercept
except Exception as e:
    print(e)
    import_exception = e


class LineTestCase(ImmTestCase):
    def test_code_check(self):
        self.code_check(["line.py"], import_exception)

    def test_no_intercept(self):
        for b in range(-10, 10):
            self.assertEqual(find_x_intercept(0, b), [])

    def test_x_intercept(self):
        for a in [2,5,10]:
            for z in range(1, 50):
                self.assertTrue(isinstance(find_x_intercept(z * 1, z * a), list), "return value of find_x_intercept should be a list")
                self.assertEqual(find_x_intercept(z * 1, z * a), [-a])


if __name__ == '__main__':
    import unittest

    unittest.main()
