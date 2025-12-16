import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge19 import odd_numbers_series


class TestOddNumbersSeries(unittest.TestCase):
    """Unit tests for odd_numbers_series function"""

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

    def test_standard_odd_series(self):
        odd_numbers_series(5)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1 3 5 7 9")

    def test_single_odd_number(self):
        odd_numbers_series(1)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1")

    # -------------------------
    # Edge Test Cases
    # -------------------------

    def test_zero_input(self):
        odd_numbers_series(0)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "")

    def test_negative_input(self):
        odd_numbers_series(-5)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "")

    # -------------------------
    # Boundary / Logical Tests
    # -------------------------

    def test_large_input(self):
        odd_numbers_series(10)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1 3 5 7 9 11 13 15 17 19")


if __name__ == "__main__":
    unittest.main()
