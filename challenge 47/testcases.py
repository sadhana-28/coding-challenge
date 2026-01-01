import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge46 import sum_of_array


class TestSumOfArray(unittest.TestCase):
    """Unit tests for sum_of_array function"""

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

    def test_standard_array(self):
        sum_of_array([1, 2, 3, 4, 5])
        output = sys.stdout.getvalue()

        self.assertIn("Sum:", output)
        self.assertIn("15", output)

    def test_single_element(self):
        sum_of_array([10])
        output = sys.stdout.getvalue()

        self.assertIn("10", output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_empty_array(self):
        sum_of_array([])
        output = sys.stdout.getvalue()

        self.assertIn("Sum:", output)
        self.assertIn("0", output)

    def test_array_with_zeroes(self):
        sum_of_array([0, 0, 0])
        output = sys.stdout.getvalue()

        self.assertIn("0", output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_array_with_negative_numbers(self):
        sum_of_array([-1, -2, -3])
        output = sys.stdout.getvalue()

        self.assertIn("-6", output)

    def test_mixed_positive_and_negative_numbers(self):
        sum_of_array([5, -2, 3, -1])
        output = sys.stdout.getvalue()

        self.assertIn("5", output)


if __name__ == "__main__":
    unittest.main()
