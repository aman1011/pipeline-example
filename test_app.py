# test_app.py
import unittest
from app import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_handle_negative_numbers(self):
        self.assertEqual(add_numbers(-2, 3), 1)

    def test_handle_zero(self):
        self.assertEqual(add_numbers(0, 3), 3)

if __name__ == '__main__':
    unittest.main()
