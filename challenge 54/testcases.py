import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge54 import binary_search


class TestBinarySearch(unittest.TestCase):
    """Unit tests for binary_search function"""

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

    def test_element_found_middle(self):
        binary_search([1, 3, 5, 7, 9], 7)
        output = sys.stdout.getvalue()

        self.assertIn("Element found at index 3", output)

    def test_element_found_first(self):
        binary_search([2, 4, 6, 8, 10], 2)
        output = sys.stdout.getvalue()

        self.assertIn("Element found at index 0", output)

    def test_element_found_last(self):
        binary_search([2, 4, 6, 8, 10], 10)
        output = sys.stdout.getvalue()

        self.assertIn("Element found at index 4", output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_single_element_found(self):
        binary_search([5], 5)
        output = sys.stdout.getvalue()

        self.assertIn("Element found at index 0", output)

    def test_single_element_not_found(self):
        binary_search([5], 3)
        output = sys.stdout.getvalue()

        self.assertIn("Element not found", output)

    def test_empty_array(self):
        binary_search([], 10)
        output = sys.stdout.getvalue()

        self.assertIn("Element not found", output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_element_not_found(self):
        binary_search([1, 3, 5, 7, 9], 4)
        output = sys.stdout.getvalue()

        self.assertIn("Element not found", output)

    def test_negative_numbers(self):
        binary_search([-10, -5, 0, 5, 10], -5)
        output = sys.stdout.getvalue()

        self.assertIn("Element found at index 1", output)

    def test_unsorted_array_behavior(self):
        # Binary search assumes sorted input.
        # This test documents current behavior without enforcing correctness.
        binary_search([5, 1, 9, 3], 3)
        output = sys.stdout.getvalue()

        # Result is undefined; we only assert that a message is printed.
        self.assertTrue(
            "Element found at index" in output or "Element not found" in output
        )


if __name__ == "__main__":
    unittest.main()
