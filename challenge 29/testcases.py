import unittest
from unittest.mock import patch
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge28 import apply_membership_discount


class TestApplyMembershipDiscount(unittest.TestCase):
    """Unit tests for apply_membership_discount function"""

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

    @patch("builtins.input", return_value="y")
    def test_membership_discount_applied(self, mock_input):
        apply_membership_discount(10000)
        output = sys.stdout.getvalue()

        # 10000 * 0.98 = 9800
        self.assertIn("₹9,800.00", output)

    @patch("builtins.input", return_value="n")
    def test_membership_discount_not_applied(self, mock_input):
        apply_membership_discount(10000)
        output = sys.stdout.getvalue()

        self.assertIn("₹10,000.00", output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    @patch("builtins.input", return_value="Y")
    def test_uppercase_input(self, mock_input):
        apply_membership_discount(5000)
        output = sys.stdout.getvalue()

        # .lower() converts 'Y' to 'y'
        self.assertIn("₹4,900.00", output)

    @patch("builtins.input", return_value="")
    def test_empty_input(self, mock_input):
        apply_membership_discount(5000)
        output = sys.stdout.getvalue()

        # No discount applied
        self.assertIn("₹5,000.00", output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    @patch("builtins.input", return_value="y")
    def test_zero_total(self, mock_input):
        apply_membership_discount(0)
        output = sys.stdout.getvalue()

        self.assertIn("₹0.00", output)

    @patch("builtins.input", return_value="y")
    def test_negative_total(self, mock_input):
        apply_membership_discount(-1000)
        output = sys.stdout.getvalue()

        # -1000 * 0.98 = -980
        self.assertIn("₹-980.00", output)


if __name__ == "__main__":
    unittest.main()
