import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge50 import count_odd_even


class TestCountOddEven(unittest.TestCase):
    """Unit tests for count_odd_even function"""

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
        count_odd_even([1, 2, 3, 4, 5, 6])
        output = sys.stdout.getvalue()

        self.assertIn("Even count: 3", output)
        self.assertIn("Odd count: 3", output)

    def test_all_even_numbers(self):
        count_odd_even([2, 4, 6, 8])
        output = sys.stdout.getvalue()

        self.assertIn("Even count: 4", output)
        self.assertIn("Odd count: 0", output)

    def test_all_odd_numbers(self):
        count_odd_even([1, 3, 5, 7])
        output = sys.stdout.getvalue()

        self.assertIn("Even count: 0", output)
        self.assertIn("Odd count: 4", output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_empty_array(self):
        count_odd_even([])
        output = sys.stdout.getvalue()

        self.assertIn("Even count: 0", output)
        self.assertIn("Odd count: 0", output)

    def test_single_even_element(self):
        count_odd_even([10])
        output = sys.stdout.getvalue()

        self.assertIn("Even count: 1", output)
        self.assertIn("Odd count: 0", output)

    def test_single_odd_element(self):
        count_odd_even([7])
        output = sys.stdout.getvalue()

        self.assertIn("Even count: 0", output)
        self.assertIn("Odd count: 1", output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_negative_numbers(self):
        count_odd_even([-1, -2, -3, -4])
        output = sys.stdout.getvalue()

        # -2 and -4 are even; -1 and -3 are odd
        self.assertIn("Even count: 2", output)
        self.assertIn("Odd count: 2", output)

    def test_mixed_zero_and_numbers(self):
        count_odd_even([0, 1, 2, 3])
        output = sys.stdout.getvalue()

        # 0 and 2 are even; 1 and 3 are odd
        self.assertIn("Even count: 2", output)
        self.assertIn("Odd count: 2", output)


if __name__ == "__main__":
    unittest.main()
