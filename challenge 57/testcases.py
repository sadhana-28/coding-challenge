import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge57 import search_2d


class TestSearch2D(unittest.TestCase):
    """Unit tests for search_2d function"""

    def setUp(self):
        self._stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self._stdout

    # -------------------------
    # Positive Test Cases
    # -------------------------

    def test_element_found(self):
        search_2d([[1, 2], [3, 4]], 3)
        output = sys.stdout.getvalue()

        self.assertIn("Element found at position 1 0", output)

    def test_element_found_first_position(self):
        search_2d([[5, 6], [7, 8]], 5)
        output = sys.stdout.getvalue()

        self.assertIn("Element found at position 0 0", output)

    def test_element_found_last_position(self):
        search_2d([[5, 6], [7, 8]], 8)
        output = sys.stdout.getvalue()

        self.assertIn("Element found at position 1 1", output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_element_not_found(self):
        search_2d([[1, 2], [3, 4]], 10)
        output = sys.stdout.getvalue()

        self.assertIn("Element not found", output)

    def test_single_element_matrix_found(self):
        search_2d([[9]], 9)
        output = sys.stdout.getvalue()

        self.assertIn("Element found at position 0 0", output)

    def test_single_element_matrix_not_found(self):
        search_2d([[9]], 5)
        output = sys.stdout.getvalue()

        self.assertIn("Element not found", output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_matrix_with_negative_numbers(self):
        search_2d([[-1, -2], [-3, -4]], -3)
        output = sys.stdout.getvalue()

        self.assertIn("Element found at position 1 0", output)

    def test_matrix_with_duplicate_values(self):
        search_2d([[1, 2], [2, 3]], 2)
        output = sys.stdout.getvalue()

        # Should return first occurrence (0,1)
        self.assertIn("Element found at position 0 1", output)

    # -------------------------
    # Error Behavior Test
    # -------------------------

    def test_empty_matrix_raises_error(self):
        # Accessing matrix[0] should raise IndexError
        with self.assertRaises(IndexError):
            search_2d([], 1)


if __name__ == "__main__":
    unittest.main()
