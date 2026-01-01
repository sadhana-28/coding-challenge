import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge41 import number_to_words


class TestNumberToWords(unittest.TestCase):
    """Unit tests for number_to_words function"""

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

    def test_standard_number(self):
        number_to_words(270176)
        output = sys.stdout.getvalue().strip()

        self.assertEqual(
            output,
            "Two Seven Zero One Seven Six"
        )

    def test_single_digit(self):
        number_to_words(5)
        output = sys.stdout.getvalue().strip()

        self.assertEqual(output, "Five")

    def test_multiple_same_digits(self):
        number_to_words(111)
        output = sys.stdout.getvalue().strip()

        self.assertEqual(output, "One One One")

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_zero(self):
        number_to_words(0)
        output = sys.stdout.getvalue().strip()

        self.assertEqual(output, "Zero")

    def test_large_number(self):
        number_to_words(9876543210)
        output = sys.stdout.getvalue().strip()

        self.assertEqual(
            output,
            "Nine Eight Seven Six Five Four Three Two One Zero"
        )

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_negative_number(self):
        # '-' is not in digit_words, so this should raise KeyError
        with self.assertRaises(KeyError):
            number_to_words(-123)

    def test_float_number(self):
        # '.' is not in digit_words, so this should raise KeyError
        with self.assertRaises(KeyError):
            number_to_words(12.5)


if __name__ == "__main__":
    unittest.main()
