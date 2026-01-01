import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge53 import sort_array


class TestSortArray(unittest.TestCase):
    """Unit tests for sort_array function"""

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

    def test_sort_ascending(self):
        arr = [4, 2, 7, 1]
        sort_array(arr, 'asc')
        output = sys.stdout.getvalue()

        self.assertIn("Sorted array:", output)
        self.assertIn("[1, 2, 4, 7]", output)

    def test_sort_descending(self):
        arr = [4, 2, 7, 1]
        sort_array(arr, 'desc')
        output = sys.stdout.getvalue()

        self.assertIn("[7, 4, 2, 1]", output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_single_element_array(self):
        arr = [10]
        sort_array(arr, 'asc')
        output = sys.stdout.getvalue()

        self.assertIn("[10]", output)

    def test_empty_array(self):
        arr = []
        sort_array(arr, 'asc')
        output = sys.stdout.getvalue()

        self.assertIn("Sorted array:", output)
        self.assertIn("[]", output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_array_with_duplicate_values(self):
        arr = [3, 1, 2, 1]
        sort_array(arr, 'asc')
        output = sys.stdout.getvalue()

        self.assertIn("[1, 1, 2, 3]", output)

    def test_array_with_negative_numbers(self):
        arr = [5, -1, 3, -10, 0]
        sort_array(arr, 'asc')
        output = sys.stdout.getvalue()

        self.assertIn("[-10, -1, 0, 3, 5]", output)

    def test_invalid_order_parameter(self):
        arr = [4, 3, 2, 1]
        sort_array(arr, 'invalid')
        output = sys.stdout.getvalue()

        # No sorting should occur if order is neither 'asc' nor 'desc'
        self.assertIn("[4, 3, 2, 1]", output)


if __name__ == "__main__":
    unittest.main()
