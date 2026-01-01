import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge42 import generate_series


class TestGenerateSeries(unittest.TestCase):
    """Unit tests for generate_series function"""

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
        generate_series(6)
        output = sys.stdout.getvalue().strip()

        # Expected: 1, -5, 9, -13, 17, -21
        self.assertEqual(output, "1 -5 9 -13 17 -21")

    def test_single_value(self):
        generate_series(1)
        output = sys.stdout.getvalue().strip()

        self.assertEqual(output, "1")

    def test_two_values(self):
        generate_series(2)
        output = sys.stdout.getvalue().strip()

        self.assertEqual(output, "1 -5")

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_zero_input(self):
        generate_series(0)
        output = sys.stdout.getvalue().strip()

        self.assertEqual(output, "")

    def test_negative_input(self):
        generate_series(-4)
        output = sys.stdout.getvalue().strip()

        self.assertEqual(output, "")

    # -------------------------
    # Boundary / Logical Tests
    # -------------------------

    def test_larger_input(self):
        generate_series(8)
        output = sys.stdout.getvalue().strip()

        self.assertEqual(output, "1 -5 9 -13 17 -21 25 -29")


if __name__ == "__main__":
    unittest.main()
