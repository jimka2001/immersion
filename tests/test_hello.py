import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "tests")))

from common import ImmTestCase, canonicalize

import_exception = None
try:
    from src.hello import hello, hello_pierre
except Exception as e:
    print(e)
    import_exception = e

class HelloTestCase(ImmTestCase):
    def test_code_check(self):
        self.code_check(["hello.py"], import_exception)


    def test_hello(self):
        self.assertEqual(hello("test"), "Hello, test!")
        self.assertEqual(hello("jim"), "Hello, jim!")

    def test_pierre(self):
        self.assertEqual(hello_pierre(), "Hello, pierre!")

if __name__ == '__main__':
    import unittest

    unittest.main()
