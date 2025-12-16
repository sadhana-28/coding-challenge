import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge43 import separate_whole_fraction


class TestSeparateWholeFraction(unittest.TestCase):
    """Unit tests for separate_whole_fraction function"""

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

    def test_standard_float_value(self):
        separate_whole_fraction(123.456)
        output = sys.stdout.getvalue()

        self.assertIn("Whole Part: 123", output)
        self.assertIn("Fractional Part: 0.456", output)

    def test_integer_input(self):
        separate_whole_fraction(100)
        output = sys.stdout.getvalue()

        self.assertIn("Whole Part: 100", output)
        self.assertIn("Fractional Part: 0", output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_zero_value(self):
        separate_whole_fraction(0.0)
        output = sys.stdout.getvalue()

        self.assertIn("Whole Part: 0", output)
        self.assertIn("Fractional Part: 0.0", output)

    def test_small_fraction(self):
        separate_whole_fraction(0.25)
        output = sys.stdout.getvalue()

        self.assertIn("Whole Part: 0", output)
        self.assertIn("Fractional Part: 0.25", output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_negative_number(self):
        separate_whole_fraction(-12.75)
        output = sys.stdout.getvalue()

        # int(-12.75) = -12 in Python
        self.assertIn("Whole Part: -12", output)
        self.assertIn("Fractional Part: -0.75", output)

    def test_float_precision_behavior(self):
        separate_whole_fraction(1.999999)
        output = sys.stdout.getvalue()

        self.assertIn("Whole Part: 1", output)
        self.assertIn("Fractional Part:", output)


if __name__ == "__main__":
    unittest.main()
