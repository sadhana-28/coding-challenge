import unittest
from unittest.mock import patch
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge26 import calculate_grand_total


class TestCalculateGrandTotal(unittest.TestCase):
    """Unit tests for calculate_grand_total function"""

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

    @patch("builtins.input", side_effect=["100", "2", "n"])
    def test_single_item(self, mock_input):
        calculate_grand_total()
        output = sys.stdout.getvalue()

        self.assertIn("Grand Total", output)
        self.assertIn("₹200.00", output)

    @patch("builtins.input", side_effect=["100", "2", "200", "1", "n"])
    def test_multiple_items(self, mock_input):
        calculate_grand_total()
        output = sys.stdout.getvalue()

        # 100*2 + 200*1 = 400
        self.assertIn("₹400.00", output)

    # -------------------------
    # Edge Test Cases
    # -------------------------

    @patch("builtins.input", side_effect=["0", "5", "n"])
    def test_zero_price(self, mock_input):
        calculate_grand_total()
        output = sys.stdout.getvalue()

        self.assertIn("₹0.00", output)

    @patch("builtins.input", side_effect=["100", "0", "n"])
    def test_zero_quantity(self, mock_input):
        calculate_grand_total()
        output = sys.stdout.getvalue()

        self.assertIn("₹0.00", output)

    # -------------------------
    # Logical / Flow Tests
    # -------------------------

    @patch("builtins.input", side_effect=["50", "2", "y", "30", "3", "y", "20", "1", "n"])
    def test_loop_continues_until_user_stops(self, mock_input):
        calculate_grand_total()
        output = sys.stdout.getvalue()

        # (50*2) + (30*3) + (20*1) = 100 + 90 + 20 = 210
        self.assertIn("₹210.00", output)


if __name__ == "__main__":
    unittest.main()
