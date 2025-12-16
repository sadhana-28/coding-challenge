import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge22 import square_series


class TestSquareSeries(unittest.TestCase):
    """Unit tests for square_series function"""

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

    def test_standard_square_series(self):
        square_series(5)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1 4 9 16 25")

    def test_single_value(self):
        square_series(1)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1")

    # -------------------------
    # Edge Test Cases
    # -------------------------

    def test_zero_input(self):
        square_series(0)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "")

    def test_negative_input(self):
        square_series(-4)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "")

    # -------------------------
    # Boundary / Logical Tests
    # -------------------------

    def test_larger_input(self):
        square_series(7)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1 4 9 16 25 36 49")


if __name__ == "__main__":
    unittest.main()
