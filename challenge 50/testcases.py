import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge49 import search_element


class TestSearchElement(unittest.TestCase):
    """Unit tests for search_element function"""

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

    def test_element_found(self):
        search_element([10, 20, 30, 40], 30)
        output = sys.stdout.getvalue()

        self.assertIn("Element found at index 2", output)

    def test_element_found_at_first_index(self):
        search_element([5, 10, 15], 5)
        output = sys.stdout.getvalue()

        self.assertIn("Element found at index 0", output)

    def test_element_found_at_last_index(self):
        search_element([5, 10, 15], 15)
        output = sys.stdout.getvalue()

        self.assertIn("Element found at index 2", output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_element_not_found(self):
        search_element([10, 20, 30], 50)
        output = sys.stdout.getvalue()

        self.assertIn("Element not found", output)

    def test_empty_array(self):
        search_element([], 10)
        output = sys.stdout.getvalue()

        self.assertIn("Element not found", output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_duplicate_elements(self):
        search_element([1, 2, 3, 2, 5], 2)
        output = sys.stdout.getvalue()

        # Should print first occurrence
        self.assertIn("Element found at index 1", output)

    def test_search_negative_value(self):
        search_element([10, -5, 20, -10], -10)
        output = sys.stdout.getvalue()

        self.assertIn("Element found at index 3", output)


if __name__ == "__main__":
    unittest.main()
