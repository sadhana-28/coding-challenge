import unittest
from unittest.mock import patch
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge45 import create_array


class TestCreateArray(unittest.TestCase):
    """Unit tests for create_array function"""

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

    @patch("builtins.input", side_effect=["3", "10", "20", "30"])
    def test_standard_array_creation(self, mock_input):
        create_array()
        output = sys.stdout.getvalue()

        self.assertIn("Array:", output)
        self.assertIn("[10, 20, 30]", output)

    @patch("builtins.input", side_effect=["1", "99"])
    def test_single_element_array(self, mock_input):
        create_array()
        output = sys.stdout.getvalue()

        self.assertIn("[99]", output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    @patch("builtins.input", side_effect=["0"])
    def test_zero_elements(self, mock_input):
        create_array()
        output = sys.stdout.getvalue()

        self.assertIn("Array:", output)
        self.assertIn("[]", output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    @patch("builtins.input", side_effect=["4", "-1", "0", "5", "10"])
    def test_array_with_negative_and_zero_values(self, mock_input):
        create_array()
        output = sys.stdout.getvalue()

        self.assertIn("[-1, 0, 5, 10]", output)


if __name__ == "__main__":
    unittest.main()
