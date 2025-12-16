import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge24 import fibonacci_series


class TestFibonacciSeries(unittest.TestCase):
    """Unit tests for fibonacci_series function"""

    def setUp(self):
        """Redirect stdout before each test"""
        self._stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        """Restore stdout after each test"""
        sys.stdout = self._stdout

    # -------------------------
    # Positive Test Cases
    # -------------------------

    def test_standard_fibonacci_series(self):
        fibonacci_series(8)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1 1 2 3 5 8 13 21")

    def test_single_element(self):
        fibonacci_series(1)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1")

    def test_two_elements(self):
        fibonacci_series(2)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1 1")

    # -------------------------
    # Edge Test Cases
    # -------------------------

    def test_zero_input(self):
        fibonacci_series(0)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "")

    def test_negative_input(self):
        fibonacci_series(-5)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "")

    # -------------------------
    # Boundary / Logical Tests
    # -------------------------

    def test_larger_input(self):
        fibonacci_series(10)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1 1 2 3 5 8 13 21 34 55")


if __name__ == "__main__":
    unittest.main()
