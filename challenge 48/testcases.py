import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge47 import find_min


class TestFindMin(unittest.TestCase):
    """Unit tests for find_min function"""

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
        find_min([4, 2, 9, 1, 7])
        output = sys.stdout.getvalue()

        self.assertIn("Minimum:", output)
        self.assertIn("1", output)

    def test_single_element_array(self):
        find_min([10])
        output = sys.stdout.getvalue()

        self.assertIn("Minimum:", output)
        self.assertIn("10", output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_all_elements_same(self):
        find_min([5, 5, 5, 5])
        output = sys.stdout.getvalue()

        self.assertIn("5", output)

    def test_sorted_descending_array(self):
        find_min([9, 7, 5, 3, 1])
        output = sys.stdout.getvalue()

        self.assertIn("1", output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_array_with_negative_numbers(self):
        find_min([-3, -1, -7, -2])
        output = sys.stdout.getvalue()

        self.assertIn("-7", output)

    def test_mixed_positive_and_negative(self):
        find_min([10, -5, 3, -20, 8])
        output = sys.stdout.getvalue()

        self.assertIn("-20", output)

    # -------------------------
    # Error Behavior Test
    # -------------------------

    def test_empty_array_raises_error(self):
        # Accessing arr[0] should raise IndexError
        with self.assertRaises(IndexError):
            find_min([])


if __name__ == "__main__":
    unittest.main()
