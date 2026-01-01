import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge52 import reverse_array


class TestReverseArray(unittest.TestCase):
    """Unit tests for reverse_array function"""

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
        arr = [1, 2, 3, 4, 5]
        reverse_array(arr)
        output = sys.stdout.getvalue()

        self.assertIn("Reversed array:", output)
        self.assertIn("[5, 4, 3, 2, 1]", output)

    def test_even_length_array(self):
        arr = [10, 20, 30, 40]
        reverse_array(arr)
        output = sys.stdout.getvalue()

        self.assertIn("[40, 30, 20, 10]", output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_single_element_array(self):
        arr = [99]
        reverse_array(arr)
        output = sys.stdout.getvalue()

        self.assertIn("[99]", output)

    def test_empty_array(self):
        arr = []
        reverse_array(arr)
        output = sys.stdout.getvalue()

        self.assertIn("Reversed array:", output)
        self.assertIn("[]", output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_array_with_negative_numbers(self):
        arr = [-1, -2, -3, -4]
        reverse_array(arr)
        output = sys.stdout.getvalue()

        self.assertIn("[-4, -3, -2, -1]", output)

    def test_array_with_duplicate_values(self):
        arr = [1, 2, 2, 3]
        reverse_array(arr)
        output = sys.stdout.getvalue()

        self.assertIn("[3, 2, 2, 1]", output)


if __name__ == "__main__":
    unittest.main()
