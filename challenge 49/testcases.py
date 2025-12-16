import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge48 import find_max


class TestFindMax(unittest.TestCase):
    """Unit tests for find_max function"""

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
        find_max([4, 2, 9, 1, 7])
        output = sys.stdout.getvalue()

        self.assertIn("Maximum:", output)
        self.assertIn("9", output)

    def test_single_element_array(self):
        find_max([10])
        output = sys.stdout.getvalue()

        self.assertIn("Maximum:", output)
        self.assertIn("10", output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_all_elements_same(self):
        find_max([5, 5, 5, 5])
        output = sys.stdout.getvalue()

        self.assertIn("5", output)

    def test_sorted_ascending_array(self):
        find_max([1, 3, 5, 7, 9])
        output = sys.stdout.getvalue()

        self.assertIn("9", output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_array_with_negative_numbers(self):
        find_max([-3, -1, -7, -2])
        output = sys.stdout.getvalue()

        self.assertIn("-1", output)

    def test_mixed_positive_and_negative(self):
        find_max([10, -5, 3, -20, 8])
        output = sys.stdout.getvalue()

        self.assertIn("10", output)

    # -------------------------
    # Error Behavior Test
    # -------------------------

    def test_empty_array_raises_error(self):
        # Accessing arr[0] should raise IndexError
        with self.assertRaises(IndexError):
            find_max([])


if __name__ == "__main__":
    unittest.main()
