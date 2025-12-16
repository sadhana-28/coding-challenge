import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge20 import even_square_series


class TestEvenSquareSeries(unittest.TestCase):
    """Unit tests for even_square_series function"""

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

    def test_standard_even_square_series(self):
        even_square_series(5)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "4 16 36 64 100")

    def test_single_value(self):
        even_square_series(1)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "4")

    # -------------------------
    # Edge Test Cases
    # -------------------------

    def test_zero_input(self):
        even_square_series(0)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "")

    def test_negative_input(self):
        even_square_series(-3)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "")

    # -------------------------
    # Boundary / Logical Tests
    # -------------------------

    def test_larger_input(self):
        even_square_series(3)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "4 16 36")


if __name__ == "__main__":
    unittest.main()
