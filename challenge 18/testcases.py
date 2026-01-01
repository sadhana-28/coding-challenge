import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge18 import natural_numbers_series


class TestNaturalNumbersSeries(unittest.TestCase):
    """Unit tests for natural_numbers_series function"""

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

    def test_standard_series(self):
        natural_numbers_series(5)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1 2 3 4 5")

    def test_single_number(self):
        natural_numbers_series(1)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1")

    # -------------------------
    # Edge Test Cases
    # -------------------------

    def test_zero_input(self):
        natural_numbers_series(0)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "")

    def test_negative_input(self):
        natural_numbers_series(-5)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "")

    # -------------------------
    # Boundary / Data Type Tests
    # -------------------------

    def test_large_input(self):
        natural_numbers_series(10)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1 2 3 4 5 6 7 8 9 10")


if __name__ == "__main__":
    unittest.main()
